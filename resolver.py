from __future__ import annotations

import logging
import time
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

from sources import threesixtyfive

import config
from mongo_store import FixtureStore
from team_aliases import aliases_for

logger = logging.getLogger("friendlies_standalone.resolver")

RESOLVE_GRACE_HOURS = 6


def _name_matches(candidate: Optional[str], names: List[str]) -> bool:
    if not candidate:
        return False
    candidate_lower = candidate.lower()
    return any(n.lower() in candidate_lower or candidate_lower in n.lower() for n in names)


def _find_match(fixture: Dict[str, Any], games: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """Two-sided match: both home AND away must line up against the
    hardcoded fixture's team names (via aliases). Single-sided matching
    is what leagues_scraper.py's threesixtyfive.filter_games_by_club_names
    uses for the leagues bucket, but that's only safe there because it's
    filtering to a known club list -- here we're matching one specific
    fixture against every friendly on earth for that day, so both sides
    must agree or a same-day coincidence (two different fixtures sharing
    one participant) could resolve wrong."""
    home_names = aliases_for(fixture["homeTeam"])
    away_names = aliases_for(fixture["awayTeam"])

    for game in games:
        game_home = (game.get("homeCompetitor") or {}).get("name")
        game_away = (game.get("awayCompetitor") or {}).get("name")

        direct = _name_matches(game_home, home_names) and _name_matches(game_away, away_names)
        swapped = _name_matches(game_home, away_names) and _name_matches(game_away, home_names)

        if direct or swapped:
            return game

    return None


def _is_past_grace_window(fixture: Dict[str, Any]) -> bool:
    kickoff_str = fixture.get("kickoffUtc")
    if not kickoff_str:
        return False
    kickoff = datetime.fromisoformat(kickoff_str.replace("Z", "+00:00"))
    return datetime.now(timezone.utc) > kickoff + timedelta(hours=RESOLVE_GRACE_HOURS)


def resolve_pending(store: FixtureStore) -> None:
    pending = store.get_fixtures_pending_resolution(source=config.FRIENDLY_SOURCE_TAG)
    if not pending:
        logger.info("No fixtures pending resolution")
        return

    logger.info(f"{len(pending)} fixture(s) pending resolution")

    by_date: Dict[str, List[Dict[str, Any]]] = {}
    for fixture in pending:
        by_date.setdefault(fixture["date"], []).append(fixture)

    for date_str, fixtures in by_date.items():
        # fetch_games_by_date_range with start_date == end_date is a
        # single call to _fetch_games_for_single_date under the hood --
        # this repo only ever resolves one day at a time (a fixture's own
        # match day), so the date-range looping that function exists for
        # never actually triggers here. Using the real shared function
        # rather than reimplementing the same request.
        games = threesixtyfive.fetch_games_by_date_range(
            config.RESOLVE_COMPETITION_IDS,
            date_str,
            date_str,
            timezone_name=config.THREESIXTYFIVE_TIMEZONE,
            user_country_id=config.THREESIXTYFIVE_USER_COUNTRY_ID,
        )
        if games is None:
            logger.error(f"365Scores fetch failed for {date_str}, skipping this cycle")
            continue

        for fixture in fixtures:
            match = _find_match(fixture, games)
            if match:
                game_id = match.get("id")
                home_competitor_id = (match.get("homeCompetitor") or {}).get("id")
                away_competitor_id = (match.get("awayCompetitor") or {}).get("id")
                competition_id = (match.get("competition") or {}).get("id")
                store.update_fixture_resolved(
                    fixture["matchId"],
                    str(game_id) if game_id is not None else None,
                    str(home_competitor_id) if home_competitor_id is not None else None,
                    str(away_competitor_id) if away_competitor_id is not None else None,
                    competition_id,
                )
                logger.info(
                    f"Resolved {fixture['homeTeam']} vs {fixture['awayTeam']} "
                    f"({date_str}) -> 365Scores game {game_id}"
                )
            elif _is_past_grace_window(fixture):
                store.abandon_fixture(fixture["matchId"])
                logger.warning(
                    f"Abandoned {fixture['homeTeam']} vs {fixture['awayTeam']} "
                    f"({date_str}) -- past grace window, no 365Scores match found"
                )
            else:
                logger.info(
                    f"No 365Scores match yet for {fixture['homeTeam']} vs "
                    f"{fixture['awayTeam']} ({date_str}) -- will retry"
                )


def run_forever(store: FixtureStore) -> None:
    logger.info(f"Resolver starting, polling every {config.RESOLVE_POLL_INTERVAL_SECONDS}s")
    while True:
        try:
            resolve_pending(store)
        except Exception:
            logger.exception("Unhandled error in resolve_pending cycle")
        time.sleep(config.RESOLVE_POLL_INTERVAL_SECONDS)
