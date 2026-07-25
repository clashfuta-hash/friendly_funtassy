from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List

# Kickoff times below are converted from the UK-time (BST, UTC+1) listings
# published by Sky Sports / ESPN / Premier League.com as of July 2026 to
# UTC (subtract 1 hour). Fixtures still "behind closed doors" or without a
# confirmed kickoff time at time of writing are left out -- add them once
# a time is confirmed rather than guessing one, since resolution matches
# on date + team names, not on time.
#
# competition_name is display-only (mirrors wembly_leagues_scrapers'
# `league` field); competition_id is filled in only once resolved.

FIXTURES: List[Dict[str, Any]] = [
    {
        "home_team": "Tottenham",
        "away_team": "Auckland FC",
        "kickoff_utc": datetime(2026, 7, 26, 3, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "Western Sydney Wanderers",
        "kickoff_utc": datetime(2026, 7, 28, 9, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Aston Villa",
        "away_team": "Real Sociedad",
        "kickoff_utc": datetime(2026, 7, 28, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Tottenham",
        "away_team": "Sydney FC",
        "kickoff_utc": datetime(2026, 7, 29, 9, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "Tottenham",
        "kickoff_utc": datetime(2026, 8, 1, 9, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Girona",
        "away_team": "Arsenal",
        "kickoff_utc": datetime(2026, 8, 1, 18, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "Juventus",
        "kickoff_utc": datetime(2026, 8, 5, 11, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Arsenal",
        "away_team": "Real Betis",
        "kickoff_utc": datetime(2026, 8, 5, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "AC Milan",
        "kickoff_utc": datetime(2026, 8, 8, 12, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Real Betis",
        "away_team": "Bournemouth",
        "kickoff_utc": datetime(2026, 8, 8, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Brighton",
        "away_team": "Roma",
        "kickoff_utc": datetime(2026, 8, 8, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Tottenham",
        "away_team": "Getafe",
        "kickoff_utc": datetime(2026, 8, 8, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
]
