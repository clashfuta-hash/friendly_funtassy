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
#
# NOTE: refreshed 2026-07-27. Everything dated 2026-07-26 or earlier has
# been dropped -- those match days have passed, and any that never
# resolved are already sitting on the Rust API as resolutionAbandoned
# (re-adding the same matchId here is a no-op; see main.py's seed_all
# docstring). List is also de-duplicated -- the previous version listed
# several fixtures twice (once under each club's section, e.g. "Arsenal
# vs Manchester City" under both Arsenal and Man City) which produced
# identical matchIds and did nothing beyond wasted /games/seed calls, so
# this version is flat and sorted by kickoff instead of grouped per-club.
#
# No club-friendly kickoff for 2026-07-27 itself was added: nothing in
# the public pre-season schedules for the tracked EPL/Serie A clubs
# could be confirmed for today at time of writing (sources checked were
# stale/contradictory -- several mixed in last year's 2025 pre-season
# results). Add one here the moment a kickoff time is confirmed, per the
# policy above -- don't guess it in to fill the gap.

FIXTURES: List[Dict[str, Any]] = [
    {
        "home_team": "Chelsea",
        "away_team": "Western Sydney Wanderers",
        "kickoff_utc": datetime(2026, 7, 28, 9, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Çaykur Rizespor",
        "away_team": "Hull City",
        "kickoff_utc": datetime(2026, 7, 28, 16, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Al Ahli",
        "away_team": "Fulham",
        "kickoff_utc": datetime(2026, 7, 28, 17, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Crystal Palace",
        "away_team": "Lens",
        "kickoff_utc": datetime(2026, 7, 28, 17, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Aston Villa",
        "away_team": "Real Sociedad",
        "kickoff_utc": datetime(2026, 7, 28, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Crystal Palace",
        "away_team": "Famalicão",
        "kickoff_utc": datetime(2026, 7, 28, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Stoke City",
        "away_team": "Everton",
        "kickoff_utc": datetime(2026, 7, 28, 18, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Tottenham Hotspur",
        "away_team": "Sydney FC",
        "kickoff_utc": datetime(2026, 7, 29, 9, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Bristol City",
        "away_team": "Newcastle United",
        "kickoff_utc": datetime(2026, 7, 29, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Ipswich Town",
        "away_team": "Osasuna",
        "kickoff_utc": datetime(2026, 7, 29, 18, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Liverpool",
        "away_team": "Wrexham",
        "kickoff_utc": datetime(2026, 7, 29, 23, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Augsburg",
        "away_team": "Bournemouth",
        "kickoff_utc": datetime(2026, 7, 30, 15, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Sunderland",
        "away_team": "Leeds United",
        "kickoff_utc": datetime(2026, 7, 30, 23, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Sporting CP",
        "away_team": "Nottingham Forest",
        "kickoff_utc": datetime(2026, 7, 31, 18, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Strasbourg",
        "away_team": "Brighton",
        "kickoff_utc": datetime(2026, 8, 1, 0, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "Tottenham Hotspur",
        "kickoff_utc": datetime(2026, 8, 1, 9, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Oxford United",
        "away_team": "Ipswich Town",
        "kickoff_utc": datetime(2026, 8, 1, 11, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester City",
        "away_team": "Inter Milan",
        "kickoff_utc": datetime(2026, 8, 1, 11, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Indonesia All-Stars",
        "away_team": "Aston Villa",
        "kickoff_utc": datetime(2026, 8, 1, 12, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester United",
        "away_team": "Atletico Madrid",
        "kickoff_utc": datetime(2026, 8, 1, 13, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Hamburg",
        "away_team": "Everton",
        "kickoff_utc": datetime(2026, 8, 1, 15, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Wycombe Wanderers",
        "away_team": "Ipswich Town",
        "kickoff_utc": datetime(2026, 8, 1, 15, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Kasımpaşa",
        "away_team": "Hull City",
        "kickoff_utc": datetime(2026, 8, 1, 16, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Girona",
        "away_team": "Arsenal",
        "kickoff_utc": datetime(2026, 8, 1, 18, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Sunderland",
        "away_team": "Wrexham",
        "kickoff_utc": datetime(2026, 8, 2, 17, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Liverpool",
        "away_team": "Leeds United",
        "kickoff_utc": datetime(2026, 8, 2, 20, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Bournemouth",
        "away_team": "Genoa",
        "kickoff_utc": datetime(2026, 8, 4, 0, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "BG Pathum United",
        "away_team": "Aston Villa",
        "kickoff_utc": datetime(2026, 8, 4, 12, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Ipswich Town",
        "away_team": "Le Havre",
        "kickoff_utc": datetime(2026, 8, 4, 18, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "AC Milan",
        "away_team": "Inter Milan",
        "kickoff_utc": datetime(2026, 8, 5, 0, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "K-League All-Stars",
        "away_team": "Manchester City",
        "kickoff_utc": datetime(2026, 8, 5, 11, 0, tzinfo=timezone.utc),
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
        "home_team": "Newcastle United",
        "away_team": "Everton",
        "kickoff_utc": datetime(2026, 8, 12, 16, 15, tzinfo=timezone.utc),
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