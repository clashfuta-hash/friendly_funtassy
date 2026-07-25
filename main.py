from __future__ import annotations

import logging
import sys

import config
from hardcoded_fixtures import FIXTURES
from mongo_store import FixtureStore
from resolver import run_forever

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger("friendlies_standalone.main")


def _build_match_id(home_team: str, away_team: str, kickoff_utc) -> str:
    import hashlib

    date_str = kickoff_utc.strftime("%Y-%m-%d")
    raw = f"{home_team}|{away_team}|{date_str}".lower()
    digest = hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]
    return f"friendly_{digest}"


def seed_all(store: FixtureStore) -> None:
    """Seed every fixture in hardcoded_fixtures.py, but ONLY on first
    creation. upsert_fixture() writes threesixtyfiveGameId into $set
    unconditionally (by design -- see its docstring: that field is meant
    to move forward as scrapers refresh odds/details for fixtures they
    discover fresh each run). This repo's fixtures are never rediscovered
    that way, so calling upsert_fixture again after the resolver has
    already filled threesixtyfiveGameId in would stomp it back to None.
    Checking get_fixture() first avoids that -- once seeded, a fixture is
    never upserted again by this repo."""
    seeded = 0
    skipped = 0
    for fixture in FIXTURES:
        match_id = _build_match_id(fixture["home_team"], fixture["away_team"], fixture["kickoff_utc"])
        if store.get_fixture(match_id):
            skipped += 1
            continue

        store.upsert_fixture(
            match_id=match_id,
            threesixtyfive_game_id=None,
            home_team=fixture["home_team"],
            away_team=fixture["away_team"],
            kickoff_utc=fixture["kickoff_utc"],
            status="upcoming",
            competition_name=fixture.get("competition_name", "Pre-Season Friendly"),
            source=config.FRIENDLY_SOURCE_TAG,
        )
        seeded += 1

    logger.info(f"Seed complete: {seeded} newly inserted, {skipped} already existed")


def main() -> None:
    if not config.MONGO_URI:
        logger.error("MONGO_URI is not set")
        sys.exit(1)

    store = FixtureStore(config.MONGO_URI)
    seed_all(store)
    run_forever(store)


if __name__ == "__main__":
    main()
