from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List

# Kickoff times below are converted from the UK-time (BST, UTC+1) or CEST
# (UTC+2) / AWST (UTC+8) listings published by Sky Sports / ESPN /
# Premier League.com / official club sites as of August 2026, to UTC.
# Fixtures still "behind closed doors" or without a confirmed kickoff
# time at time of writing are left out -- add them once a time is
# confirmed rather than guessing one, since resolution matches on
# date + team names, not on time.
#
# competition_name is display-only (mirrors wembly_leagues_scrapers'
# `league` field); competition_id is filled in only once resolved.
#
# NOTE: refreshed 2026-08-06. Everything dated 2026-08-05 or earlier has
# been dropped -- those match days are in the past as of today, and any
# that never resolved are already sitting on the Rust API as
# resolutionAbandoned (re-adding the same matchId here is a no-op; see
# main.py's seed_all docstring).
#
# This refresh also adds EPL + Serie A friendlies through 2026-08-20
# (Premier League season starts 2026-08-21; Serie A starts 2026-08-22,
# so the pre-season friendly calendar is essentially exhausted by the
# 16th-17th -- nothing further could be confirmed for the 2026-08-17
# through 2026-08-20 window at time of writing; don't guess one in to
# fill the gap, add it once a source confirms it).

FIXTURES: List[Dict[str, Any]] = [
    {
        "home_team": "Bayern Munich",
        "away_team": "Aston Villa",
        "kickoff_utc": datetime(2026, 8, 7, 12, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Juventus",
        "away_team": "Inter Milan",
        "kickoff_utc": datetime(2026, 8, 8, 0, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Lens",
        "away_team": "Sunderland",
        "kickoff_utc": datetime(2026, 8, 8, 10, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "AC Milan",
        "kickoff_utc": datetime(2026, 8, 8, 12, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Eintracht Frankfurt",
        "away_team": "Hull City",
        "kickoff_utc": datetime(2026, 8, 8, 13, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Leeds United",
        "away_team": "RB Leipzig",
        "kickoff_utc": datetime(2026, 8, 8, 13, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Brighton",
        "away_team": "Roma",
        "kickoff_utc": datetime(2026, 8, 8, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Ipswich Town",
        "away_team": "Rayo Vallecano",
        "kickoff_utc": datetime(2026, 8, 8, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Tottenham Hotspur",
        "away_team": "Getafe",
        "kickoff_utc": datetime(2026, 8, 8, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Coventry City",
        "away_team": "Espanyol",
        "kickoff_utc": datetime(2026, 8, 8, 16, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester United",
        "away_team": "Paris Saint-Germain",
        "kickoff_utc": datetime(2026, 8, 8, 15, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Stuttgart",
        "away_team": "Everton",
        "kickoff_utc": datetime(2026, 8, 8, 15, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Rennes",
        "away_team": "Brentford",
        "kickoff_utc": datetime(2026, 8, 8, 16, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Udinese",
        "away_team": "Nottingham Forest",
        "kickoff_utc": datetime(2026, 8, 8, 18, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Barcelona",
        "away_team": "Nottingham Forest",
        "kickoff_utc": datetime(2026, 8, 8, 19, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Real Betis",
        "away_team": "Bournemouth",
        "kickoff_utc": datetime(2026, 8, 8, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Valencia",
        "away_team": "Newcastle United",
        "kickoff_utc": datetime(2026, 8, 8, 19, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Napoli",
        "away_team": "Celta Vigo",
        "kickoff_utc": datetime(2026, 8, 8, 19, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester City",
        "away_team": "Atletico Madrid",
        "kickoff_utc": datetime(2026, 8, 9, 11, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Johor Darul Ta'zim",
        "away_team": "Chelsea",
        "kickoff_utc": datetime(2026, 8, 9, 12, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Arsenal",
        "away_team": "Borussia Dortmund",
        "kickoff_utc": datetime(2026, 8, 9, 13, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Liverpool",
        "away_team": "Monaco",
        "kickoff_utc": datetime(2026, 8, 9, 13, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Juventus",
        "away_team": "Palermo",
        "kickoff_utc": datetime(2026, 8, 11, 10, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Newcastle United",
        "away_team": "Everton",
        "kickoff_utc": datetime(2026, 8, 12, 16, 15, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Napoli",
        "away_team": "Aris Thessaloniki",
        "kickoff_utc": datetime(2026, 8, 12, 19, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Arsenal",
        "away_team": "Como",
        "kickoff_utc": datetime(2026, 8, 12, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester United",
        "away_team": "Leeds United",
        "kickoff_utc": datetime(2026, 8, 12, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Nottingham Forest",
        "away_team": "Bayer Leverkusen",
        "kickoff_utc": datetime(2026, 8, 12, 18, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Coventry City",
        "away_team": "Monaco",
        "kickoff_utc": datetime(2026, 8, 14, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Freiburg",
        "away_team": "Crystal Palace",
        "kickoff_utc": datetime(2026, 8, 15, 12, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "Real Sociedad",
        "kickoff_utc": datetime(2026, 8, 15, 13, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Borussia Monchengladbach",
        "away_team": "Aston Villa",
        "kickoff_utc": datetime(2026, 8, 15, 13, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Mainz",
        "away_team": "Bournemouth",
        "kickoff_utc": datetime(2026, 8, 15, 13, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Union Berlin",
        "away_team": "Ipswich Town",
        "kickoff_utc": datetime(2026, 8, 15, 13, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Borussia Dortmund",
        "away_team": "Roma",
        "kickoff_utc": datetime(2026, 8, 15, 15, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Brentford",
        "away_team": "Eintracht Frankfurt",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Brighton",
        "away_team": "Bologna",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Everton",
        "away_team": "Lille",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Hull City",
        "away_team": "Nice",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Leeds United",
        "away_team": "Augsburg",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Newcastle United",
        "away_team": "Bayer Leverkusen",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Sunderland",
        "away_team": "Rennes",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Tottenham Hotspur",
        "away_team": "Hoffenheim",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester United",
        "away_team": "AC Milan",
        "kickoff_utc": datetime(2026, 8, 15, 14, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Fulham",
        "away_team": "Stuttgart",
        "kickoff_utc": datetime(2026, 8, 15, 15, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Tottenham Hotspur",
        "away_team": "Hoffenheim",
        "kickoff_utc": datetime(2026, 8, 16, 11, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Nottingham Forest",
        "away_team": "Brest",
        "kickoff_utc": datetime(2026, 8, 16, 13, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Arsenal",
        "away_team": "Manchester City",
        "kickoff_utc": datetime(2026, 8, 16, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Community Shield",
    },
    {
        "home_team": "Newcastle United",
        "away_team": "Strasbourg",
        "kickoff_utc": datetime(2026, 8, 16, 15, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Liverpool",
        "away_team": "Como",
        "kickoff_utc": datetime(2026, 8, 16, 17, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
]
