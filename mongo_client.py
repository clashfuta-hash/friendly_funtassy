from __future__ import annotations

import hashlib
import logging
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Optional

from pymongo import MongoClient
from pymongo.collection import Collection

import config

logger = logging.getLogger("friendlies.mongo")


def build_match_id(home_team: str, away_team: str, kickoff_utc: datetime) -> str:
    date_str = kickoff_utc.strftime("%Y-%m-%d")
    raw = f"{home_team}|{away_team}|{date_str}".lower()
    digest = hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]
    return f"friendly_{digest}"


class FriendlyStore:
    def __init__(self, mongo_uri: str):
        self._client = MongoClient(mongo_uri)
        self._collection: Collection = self._client[config.MONGO_DB][config.MONGO_COLLECTION]
        self._ensure_indexes()

    def _ensure_indexes(self):
        try:
            self._collection.create_index("matchId", unique=True)
            self._collection.create_index("threesixtyfiveGameId")
            self._collection.create_index("source")
            self._collection.create_index("kickoffUtc")
        except Exception as e:
            logger.warning(f"Index creation issue: {e}")

    def seed_fixture(self, fixture: Dict[str, Any]) -> bool:
        """Upsert a hardcoded fixture. Only writes fields this repo owns
        (`status`/`isLive`/etc. are left to $setOnInsert, exactly like
        wembly_leagues_scrapers' upsert_fixture, so re-seeding never
        stomps state the main poller has since moved forward)."""
        home_team = fixture["home_team"]
        away_team = fixture["away_team"]
        kickoff_utc: datetime = fixture["kickoff_utc"]
        competition_name = fixture.get("competition_name", "Pre-Season Friendly")

        match_id = build_match_id(home_team, away_team, kickoff_utc)
        date_str = kickoff_utc.strftime("%Y-%m-%d")
        time_str = kickoff_utc.strftime("%H:%M")

        doc = {
            "matchId": match_id,
            "homeTeam": home_team,
            "awayTeam": away_team,
            "league": competition_name,
            "date": date_str,
            "time": time_str,
            "kickoffUtc": kickoff_utc.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"),
            "source": config.SOURCE_TAG,
            "lastSeededAt": datetime.now(timezone.utc),
        }

        set_on_insert = {
            "_id": match_id,
            "status": "upcoming",
            "isLive": False,
            "availableForVoting": True,
            "threesixtyfiveGameId": None,
            "home_competitor_id": None,
            "away_competitor_id": None,
            "competition_id": None,
            "resolutionAbandoned": False,
            "homeScore": None,
            "awayScore": None,
            "homeWin": 1.0,
            "awayWin": 1.0,
            "draw": 1.0,
            "votes": 0,
            "voters": [],
            "comments": 0,
            "commentary": [],
            "commentaryCount": 0,
            "lastCommentaryAt": None,
            "lineups": None,
            "lineupsFetched": False,
            "lineupsFetchedAt": None,
            "statistics": [],
            "lastStatisticsMinute": None,
            "forwardedEventSignatures": [],
            "lastPolledAt": None,
            "completedAt": None,
            "movedToHistory": False,
            "createdAt": datetime.now(timezone.utc),
            "result": None,
            "timeElapsed": None,
        }

        result = self._collection.update_one(
            {"matchId": match_id},
            {"$set": doc, "$setOnInsert": set_on_insert},
            upsert=True,
        )
        return result.upserted_id is not None

    def get_fixtures_pending_resolution(self) -> List[Dict[str, Any]]:
        today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        return list(
            self._collection.find(
                {
                    "source": config.SOURCE_TAG,
                    "threesixtyfiveGameId": None,
                    "date": {"$lte": today_str},
                    "resolutionAbandoned": {"$ne": True},
                }
            )
        )

    def update_fixture_resolved(
        self,
        match_id: str,
        threesixtyfive_game_id: str,
        home_competitor_id: Optional[str],
        away_competitor_id: Optional[str],
        competition_id: Optional[int],
    ) -> None:
        self._collection.update_one(
            {"matchId": match_id},
            {
                "$set": {
                    "threesixtyfiveGameId": threesixtyfive_game_id,
                    "home_competitor_id": home_competitor_id,
                    "away_competitor_id": away_competitor_id,
                    "competition_id": competition_id,
                    "resolvedAt": datetime.now(timezone.utc),
                }
            },
        )
        logger.info(f"Resolved {match_id} -> 365Scores game {threesixtyfive_game_id}")

    def abandon_fixture(self, match_id: str) -> None:
        self._collection.update_one(
            {"matchId": match_id},
            {"$set": {"resolutionAbandoned": True, "resolutionAbandonedAt": datetime.now(timezone.utc)}},
        )
        logger.warning(f"Abandoned resolution for {match_id} -- past grace window, no 365Scores match found")

    def is_past_grace_window(self, fixture: Dict[str, Any]) -> bool:
        kickoff_str = fixture.get("kickoffUtc")
        if not kickoff_str:
            return False
        kickoff = datetime.fromisoformat(kickoff_str.replace("Z", "+00:00"))
        return datetime.now(timezone.utc) > kickoff + timedelta(hours=config.RESOLVE_GRACE_HOURS)
