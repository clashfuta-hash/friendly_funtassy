"""
Rust-backed persistence client for the friendly-fixtures resolver.
Replaces mongo_store.py / mongo_client.py entirely -- this process
never opens a DB connection, only talks to config.FANCLASH_API.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger("friendlies_standalone.rust_client")


class RustClient:
    def __init__(self, api_url: str, timeout: int = 30, max_retries: int = 3):
        self.api_url = api_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "FriendliesResolver/1.0",
            }
        )
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["POST", "PUT", "GET", "DELETE"],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def _post(self, endpoint: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        url = f"{self.api_url}{endpoint}"
        try:
            resp = self.session.post(url, json=data, timeout=self.timeout)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"POST {endpoint} failed: {e}")
            if hasattr(e, "response") and e.response is not None:
                logger.error(f"Response: {e.response.text[:500]}")
            return None

    def _get(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Any]:
        url = f"{self.api_url}{endpoint}"
        try:
            resp = self.session.get(url, params=params, timeout=self.timeout)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"GET {endpoint} failed: {e}")
            return None

    def _format_timestamp(self, ts) -> str:
        if isinstance(ts, datetime):
            return (
                ts.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
            )
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    # ================================================================
    # SEEDING
    # ================================================================

    def seed_fixture(
        self,
        match_id: str,
        home_team: str,
        away_team: str,
        kickoff_utc: datetime,
        competition_name: str,
        source: str,
        target_collection: str = "games",
    ) -> bool:
        """target_collection: "games" for domestic league/club friendlies,
        "fixtures" for internationals. Sent to the Rust API so /games/seed
        writes (and idempotency-checks) the correct collection pair --
        games/games_history vs fixtures/fixtures_history -- instead of
        always defaulting to fixtures. See rust API's seed_fixture handler."""
        payload = {
            "matchId": match_id,
            "homeTeam": home_team,
            "awayTeam": away_team,
            "league": competition_name,
            "kickoffUtc": self._format_timestamp(kickoff_utc),
            "date": kickoff_utc.strftime("%Y-%m-%d"),
            "time": kickoff_utc.strftime("%H:%M"),
            "dateIso": kickoff_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source": source,
            "targetCollection": target_collection,
        }
        result = self._post("/games/seed", payload)
        if result is None:
            return False
        logger.debug(f"seed_fixture({match_id}): created={result.get('created')}")
        return True

    # ================================================================
    # RESOLUTION
    # ================================================================

    def get_fixtures_pending_resolution(self, source: str) -> List[Dict[str, Any]]:
        result = self._get("/games/pending-resolution", {"source": source})
        return result if isinstance(result, list) else []

    def update_fixture_resolved(
        self,
        match_id: str,
        threesixtyfive_game_id: Optional[str],
        home_competitor_id: Optional[str],
        away_competitor_id: Optional[str],
        competition_id: Optional[int],
    ) -> bool:
        payload = {
            "threesixtyfiveGameId": threesixtyfive_game_id,
            "home_competitor_id": home_competitor_id,
            "away_competitor_id": away_competitor_id,
            "competition_id": competition_id,
        }
        result = self._post(f"/games/{match_id}/resolve", payload)
        return result is not None

    def abandon_fixture(self, match_id: str) -> bool:
        result = self._post(f"/games/{match_id}/abandon", {})
        return result is not None
