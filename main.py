from __future__ import annotations

import logging
import sys

import config
from hardcoded_fixtures import FIXTURES
from rust_client import RustClient
from resolver import resolve_pending

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


def seed_all(client: RustClient) -> None:
    """Idempotency moved server-side -- /games/seed no-ops if matchId
    already exists, so this no longer needs a get_fixture() pre-check."""
    seeded = 0
    for fixture in FIXTURES:
        match_id = _build_match_id(
            fixture["home_team"], fixture["away_team"], fixture["kickoff_utc"]
        )
        ok = client.seed_fixture(
            match_id=match_id,
            home_team=fixture["home_team"],
            away_team=fixture["away_team"],
            kickoff_utc=fixture["kickoff_utc"],
            competition_name=fixture.get("competition_name", "Pre-Season Friendly"),
            source=config.FRIENDLY_SOURCE_TAG,
            # This file is domestic club friendlies (EPL/Serie A pre-season
            # clubs), not internationals -- must land in games/games_history,
            # not fixtures/fixtures_history. Override per-fixture below if a
            # non-domestic friendly is ever added to FIXTURES.
            target_collection=fixture.get("target_collection", "games"),
        )
        if ok:
            seeded += 1
        else:
            logger.error(
                f"Failed to seed {match_id} -- Rust API unreachable or rejected"
            )

    logger.info(f"Seed pass complete: {seeded}/{len(FIXTURES)} confirmed with Rust API")


def main() -> None:
    if not config.FANCLASH_API:
        logger.error("FANCLASH_API is not set")
        sys.exit(1)

    client = RustClient(config.FANCLASH_API)
    seed_all(client)

    try:
        resolve_pending(client)
    except Exception:
        logger.exception("Unhandled error in resolve_pending")
        sys.exit(1)


if __name__ == "__main__":
    main()
