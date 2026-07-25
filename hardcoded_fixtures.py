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
    # === PREMIER LEAGUE FIXTURES ===
    # Source: Sky Sports, Sports Illustrated, Premier League official [citation:1][citation:5][citation:12]
    # Arsenal
    {
        "home_team": "Girona",
        "away_team": "Arsenal",
        "kickoff_utc": datetime(
            2026, 8, 1, 18, 0, tzinfo=timezone.utc
        ),  # 7pm BST = 6pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Arsenal",
        "away_team": "Real Betis",
        "kickoff_utc": datetime(
            2026, 8, 5, 18, 30, tzinfo=timezone.utc
        ),  # 7:30pm BST = 6:30pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Arsenal",
        "away_team": "Borussia Dortmund",
        "kickoff_utc": datetime(
            2026, 8, 9, 13, 0, tzinfo=timezone.utc
        ),  # 2pm BST = 1pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Arsenal",
        "away_team": "Como",
        "kickoff_utc": datetime(
            2026, 8, 12, 18, 30, tzinfo=timezone.utc
        ),  # 7:30pm BST = 6:30pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Arsenal",
        "away_team": "Manchester City",
        "kickoff_utc": datetime(
            2026, 8, 16, 14, 0, tzinfo=timezone.utc
        ),  # 3pm BST = 2pm UTC
        "competition_name": "Community Shield",
    },
    # Aston Villa [citation:1][citation:5]
    {
        "home_team": "Walsall",
        "away_team": "Aston Villa",
        "kickoff_utc": datetime(
            2026, 7, 21, 18, 30, tzinfo=timezone.utc
        ),  # 7:30pm BST = 6:30pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Porto",
        "away_team": "Aston Villa",
        "kickoff_utc": datetime(
            2026, 7, 25, 18, 0, tzinfo=timezone.utc
        ),  # 7pm BST = 6pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Aston Villa",
        "away_team": "Real Sociedad",
        "kickoff_utc": datetime(2026, 7, 28, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Indonesia All-Stars",
        "away_team": "Aston Villa",
        "kickoff_utc": datetime(
            2026, 8, 1, 12, 0, tzinfo=timezone.utc
        ),  # 1pm BST = 12pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "BG Pathum United",
        "away_team": "Aston Villa",
        "kickoff_utc": datetime(
            2026, 8, 4, 12, 30, tzinfo=timezone.utc
        ),  # 1:30pm BST = 12:30pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Bayern Munich",
        "away_team": "Aston Villa",
        "kickoff_utc": datetime(
            2026, 8, 7, 12, 0, tzinfo=timezone.utc
        ),  # 1pm BST = 12pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Borussia Monchengladbach",
        "away_team": "Aston Villa",
        "kickoff_utc": datetime(
            2026, 8, 15, 13, 30, tzinfo=timezone.utc
        ),  # 2:30pm BST = 1:30pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    # Bournemouth [citation:1][citation:5]
    {
        "home_team": "St. Pauli",
        "away_team": "Bournemouth",
        "kickoff_utc": datetime(
            2026, 7, 24, 15, 0, tzinfo=timezone.utc
        ),  # 4pm BST = 3pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Augsburg",
        "away_team": "Bournemouth",
        "kickoff_utc": datetime(2026, 7, 30, 15, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Bournemouth",
        "away_team": "Genoa",
        "kickoff_utc": datetime(
            2026, 8, 4, 0, 0, tzinfo=timezone.utc
        ),  # behind closed doors, time TBC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Real Betis",
        "away_team": "Bournemouth",
        "kickoff_utc": datetime(2026, 8, 8, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Mainz",
        "away_team": "Bournemouth",
        "kickoff_utc": datetime(2026, 8, 15, 13, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Brentford [citation:1][citation:5]
    {
        "home_team": "Rennes",
        "away_team": "Brentford",
        "kickoff_utc": datetime(
            2026, 8, 8, 16, 0, tzinfo=timezone.utc
        ),  # 5pm BST = 4pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Brentford",
        "away_team": "Eintracht Frankfurt",
        "kickoff_utc": datetime(
            2026, 8, 15, 14, 0, tzinfo=timezone.utc
        ),  # 3pm BST = 2pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    # Brighton [citation:1][citation:5]
    {
        "home_team": "Annecy",
        "away_team": "Brighton",
        "kickoff_utc": datetime(
            2026, 7, 25, 0, 0, tzinfo=timezone.utc
        ),  # behind closed doors, time TBC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Strasbourg",
        "away_team": "Brighton",
        "kickoff_utc": datetime(
            2026, 8, 1, 0, 0, tzinfo=timezone.utc
        ),  # behind closed doors, time TBC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Brighton",
        "away_team": "Roma",
        "kickoff_utc": datetime(2026, 8, 8, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Brighton",
        "away_team": "Bologna",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Chelsea [citation:1][citation:5][citation:12]
    {
        "home_team": "Chelsea",
        "away_team": "Western Sydney Wanderers",
        "kickoff_utc": datetime(2026, 7, 28, 9, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "Tottenham Hotspur",
        "kickoff_utc": datetime(2026, 8, 1, 9, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "Juventus",
        "kickoff_utc": datetime(2026, 8, 5, 11, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "AC Milan",
        "kickoff_utc": datetime(2026, 8, 8, 12, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Johor Darul Ta'zim",
        "away_team": "Chelsea",
        "kickoff_utc": datetime(
            2026, 8, 9, 12, 0, tzinfo=timezone.utc
        ),  # 1pm BST = 12pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "Real Sociedad",
        "kickoff_utc": datetime(
            2026, 8, 15, 13, 0, tzinfo=timezone.utc
        ),  # 2pm BST = 1pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    # Crystal Palace [citation:1][citation:5]
    {
        "home_team": "Bromley",
        "away_team": "Crystal Palace",
        "kickoff_utc": datetime(
            2026, 7, 25, 14, 0, tzinfo=timezone.utc
        ),  # 3pm BST = 2pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Crystal Palace",
        "away_team": "Lens",
        "kickoff_utc": datetime(
            2026, 7, 28, 17, 0, tzinfo=timezone.utc
        ),  # 6pm BST = 5pm UTC, 45-min match
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Crystal Palace",
        "away_team": "Famalicão",
        "kickoff_utc": datetime(
            2026, 7, 28, 18, 30, tzinfo=timezone.utc
        ),  # 7:30pm BST = 6:30pm UTC, 45-min match
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Freiburg",
        "away_team": "Crystal Palace",
        "kickoff_utc": datetime(
            2026, 8, 15, 12, 0, tzinfo=timezone.utc
        ),  # 1pm BST = 12pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    # Everton [citation:1][citation:5]
    {
        "home_team": "Dundee",
        "away_team": "Everton",
        "kickoff_utc": datetime(
            2026, 7, 18, 13, 0, tzinfo=timezone.utc
        ),  # 2pm BST = 1pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Bolton Wanderers",
        "away_team": "Everton",
        "kickoff_utc": datetime(2026, 7, 25, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Stoke City",
        "away_team": "Everton",
        "kickoff_utc": datetime(
            2026, 7, 28, 18, 45, tzinfo=timezone.utc
        ),  # 7:45pm BST = 6:45pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Hamburg",
        "away_team": "Everton",
        "kickoff_utc": datetime(
            2026, 8, 1, 15, 0, tzinfo=timezone.utc
        ),  # 4pm BST = 3pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Stuttgart",
        "away_team": "Everton",
        "kickoff_utc": datetime(2026, 8, 8, 15, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Newcastle United",
        "away_team": "Everton",
        "kickoff_utc": datetime(
            2026, 8, 12, 16, 15, tzinfo=timezone.utc
        ),  # 5:15pm BST = 4:15pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Everton",
        "away_team": "Lille",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Fulham [citation:1][citation:5]
    {
        "home_team": "Al Ahli",
        "away_team": "Fulham",
        "kickoff_utc": datetime(
            2026, 7, 28, 17, 0, tzinfo=timezone.utc
        ),  # 6pm BST = 5pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Fulham",
        "away_team": "Stuttgart",
        "kickoff_utc": datetime(
            2026, 8, 15, 15, 0, tzinfo=timezone.utc
        ),  # 4pm BST = 3pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    # Hull City [citation:1][citation:5]
    {
        "home_team": "Konyaspor",
        "away_team": "Hull City",
        "kickoff_utc": datetime(
            2026, 7, 25, 15, 30, tzinfo=timezone.utc
        ),  # 4:30pm BST = 3:30pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Çaykur Rizespor",
        "away_team": "Hull City",
        "kickoff_utc": datetime(
            2026, 7, 28, 16, 0, tzinfo=timezone.utc
        ),  # 5pm BST = 4pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Kasımpaşa",
        "away_team": "Hull City",
        "kickoff_utc": datetime(
            2026, 8, 1, 16, 0, tzinfo=timezone.utc
        ),  # 5pm BST = 4pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Eintracht Frankfurt",
        "away_team": "Hull City",
        "kickoff_utc": datetime(
            2026, 8, 8, 13, 0, tzinfo=timezone.utc
        ),  # 2pm BST = 1pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Hull City",
        "away_team": "Nice",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Ipswich Town [citation:1][citation:5]
    {
        "home_team": "Ipswich Town",
        "away_team": "Osasuna",
        "kickoff_utc": datetime(
            2026, 7, 29, 18, 45, tzinfo=timezone.utc
        ),  # 7:45pm BST = 6:45pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Oxford United",
        "away_team": "Ipswich Town",
        "kickoff_utc": datetime(
            2026, 8, 1, 11, 0, tzinfo=timezone.utc
        ),  # 12pm BST = 11am UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Wycombe Wanderers",
        "away_team": "Ipswich Town",
        "kickoff_utc": datetime(
            2026, 8, 1, 15, 0, tzinfo=timezone.utc
        ),  # 4pm BST = 3pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Ipswich Town",
        "away_team": "Le Havre",
        "kickoff_utc": datetime(
            2026, 8, 4, 18, 45, tzinfo=timezone.utc
        ),  # 7:45pm BST = 6:45pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Ipswich Town",
        "away_team": "Rayo Vallecano",
        "kickoff_utc": datetime(2026, 8, 8, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Union Berlin",
        "away_team": "Ipswich Town",
        "kickoff_utc": datetime(
            2026, 8, 15, 13, 30, tzinfo=timezone.utc
        ),  # 2:30pm BST = 1:30pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    # Leeds United [citation:1][citation:5][citation:12]
    {
        "home_team": "Wrexham",
        "away_team": "Leeds United",
        "kickoff_utc": datetime(
            2026, 7, 25, 23, 30, tzinfo=timezone.utc
        ),  # 12:30am BST July 26 = 11:30pm UTC July 25
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Sunderland",
        "away_team": "Leeds United",
        "kickoff_utc": datetime(
            2026, 7, 30, 23, 30, tzinfo=timezone.utc
        ),  # 12:30am BST July 31 = 11:30pm UTC July 30
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Liverpool",
        "away_team": "Leeds United",
        "kickoff_utc": datetime(
            2026, 8, 2, 20, 0, tzinfo=timezone.utc
        ),  # 9pm BST = 8pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Leeds United",
        "away_team": "RB Leipzig",
        "kickoff_utc": datetime(2026, 8, 8, 13, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester United",
        "away_team": "Leeds United",
        "kickoff_utc": datetime(2026, 8, 12, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Leeds United",
        "away_team": "Augsburg",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Liverpool [citation:1][citation:5][citation:12]
    {
        "home_team": "Liverpool",
        "away_team": "Sunderland",
        "kickoff_utc": datetime(
            2026, 7, 25, 22, 0, tzinfo=timezone.utc
        ),  # 11pm BST = 10pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Liverpool",
        "away_team": "Wrexham",
        "kickoff_utc": datetime(
            2026, 7, 29, 23, 30, tzinfo=timezone.utc
        ),  # 12:30am BST July 30 = 11:30pm UTC July 29
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Liverpool",
        "away_team": "Leeds United",
        "kickoff_utc": datetime(2026, 8, 2, 20, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Liverpool",
        "away_team": "Monaco",
        "kickoff_utc": datetime(
            2026, 8, 9, 13, 30, tzinfo=timezone.utc
        ),  # 2:30pm BST = 1:30pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Liverpool",
        "away_team": "Como",
        "kickoff_utc": datetime(
            2026, 8, 16, 17, 0, tzinfo=timezone.utc
        ),  # 6pm BST = 5pm UTC, Anfield
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Liverpool",
        "away_team": "Como",
        "kickoff_utc": datetime(
            2026, 8, 16, 0, 0, tzinfo=timezone.utc
        ),  # behind closed doors, time TBC
        "competition_name": "Pre-Season Friendly",
    },
    # Manchester City [citation:1][citation:5][citation:12]
    {
        "home_team": "Manchester City",
        "away_team": "Inter Milan",
        "kickoff_utc": datetime(
            2026, 8, 1, 11, 30, tzinfo=timezone.utc
        ),  # 12:30pm BST = 11:30am UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "K-League All-Stars",
        "away_team": "Manchester City",
        "kickoff_utc": datetime(
            2026, 8, 5, 11, 0, tzinfo=timezone.utc
        ),  # 12pm BST = 11am UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester City",
        "away_team": "Atletico Madrid",
        "kickoff_utc": datetime(2026, 8, 9, 11, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Arsenal",
        "away_team": "Manchester City",
        "kickoff_utc": datetime(2026, 8, 16, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Community Shield",
    },
    # Manchester United [citation:1][citation:5][citation:12]
    {
        "home_team": "Manchester United",
        "away_team": "Wrexham",
        "kickoff_utc": datetime(
            2026, 7, 18, 16, 0, tzinfo=timezone.utc
        ),  # 5pm BST = 4pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Rosenborg",
        "away_team": "Manchester United",
        "kickoff_utc": datetime(2026, 7, 24, 16, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester United",
        "away_team": "Atletico Madrid",
        "kickoff_utc": datetime(
            2026, 8, 1, 13, 0, tzinfo=timezone.utc
        ),  # 2pm BST = 1pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester United",
        "away_team": "Paris Saint-Germain",
        "kickoff_utc": datetime(
            2026, 8, 8, 15, 0, tzinfo=timezone.utc
        ),  # 4pm BST = 3pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester United",
        "away_team": "Leeds United",
        "kickoff_utc": datetime(2026, 8, 12, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester United",
        "away_team": "AC Milan",
        "kickoff_utc": datetime(
            2026, 8, 15, 14, 45, tzinfo=timezone.utc
        ),  # 3:45pm BST = 2:45pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    # Newcastle United [citation:1][citation:5][citation:12]
    {
        "home_team": "Gateshead",
        "away_team": "Newcastle United",
        "kickoff_utc": datetime(
            2026, 7, 25, 11, 30, tzinfo=timezone.utc
        ),  # 12:30pm BST = 11:30am UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Bristol City",
        "away_team": "Newcastle United",
        "kickoff_utc": datetime(2026, 7, 29, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Valencia",
        "away_team": "Newcastle United",
        "kickoff_utc": datetime(
            2026, 8, 8, 19, 0, tzinfo=timezone.utc
        ),  # 8pm BST = 7pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Newcastle United",
        "away_team": "Everton",
        "kickoff_utc": datetime(2026, 8, 12, 16, 15, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Newcastle United",
        "away_team": "Bayer Leverkusen",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Newcastle United",
        "away_team": "Strasbourg",
        "kickoff_utc": datetime(
            2026, 8, 16, 15, 0, tzinfo=timezone.utc
        ),  # 4pm BST = 3pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    # Nottingham Forest [citation:1][citation:5][citation:12]
    {
        "home_team": "Notts County",
        "away_team": "Nottingham Forest",
        "kickoff_utc": datetime(
            2026, 7, 18, 14, 0, tzinfo=timezone.utc
        ),  # 3pm BST = 2pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Nottingham Forest",
        "away_team": "Blackburn Rovers",
        "kickoff_utc": datetime(
            2026, 7, 22, 10, 0, tzinfo=timezone.utc
        ),  # 11am BST = 10am UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Vitoria de Guimaraes",
        "away_team": "Nottingham Forest",
        "kickoff_utc": datetime(
            2026, 7, 26, 19, 0, tzinfo=timezone.utc
        ),  # 8pm BST = 7pm UTC, behind closed doors
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Sporting CP",
        "away_team": "Nottingham Forest",
        "kickoff_utc": datetime(2026, 7, 31, 18, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Udinese",
        "away_team": "Nottingham Forest",
        "kickoff_utc": datetime(
            2026, 8, 8, 18, 0, tzinfo=timezone.utc
        ),  # 7pm BST = 6pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Nottingham Forest",
        "away_team": "Bayer Leverkusen",
        "kickoff_utc": datetime(2026, 8, 12, 18, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Nottingham Forest",
        "away_team": "Brest",
        "kickoff_utc": datetime(
            2026, 8, 16, 13, 0, tzinfo=timezone.utc
        ),  # 2pm BST = 1pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    # Sunderland [citation:1][citation:5][citation:12]
    {
        "home_team": "Sunderland",
        "away_team": "Liverpool",
        "kickoff_utc": datetime(2026, 7, 25, 22, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Sunderland",
        "away_team": "Leeds United",
        "kickoff_utc": datetime(2026, 7, 30, 23, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Sunderland",
        "away_team": "Wrexham",
        "kickoff_utc": datetime(
            2026, 8, 2, 17, 0, tzinfo=timezone.utc
        ),  # 6pm BST = 5pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Lens",
        "away_team": "Sunderland",
        "kickoff_utc": datetime(
            2026, 8, 8, 10, 0, tzinfo=timezone.utc
        ),  # 11am BST = 10am UTC, behind closed doors
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Lens",
        "away_team": "Sunderland",
        "kickoff_utc": datetime(
            2026, 8, 8, 15, 0, tzinfo=timezone.utc
        ),  # 4pm BST = 3pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Sunderland",
        "away_team": "Rennes",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Tottenham Hotspur [citation:1][citation:5][citation:12]
    {
        "home_team": "Tottenham Hotspur",
        "away_team": "Auckland FC",
        "kickoff_utc": datetime(
            2026, 7, 26, 3, 0, tzinfo=timezone.utc
        ),  # 4am BST = 3am UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Tottenham Hotspur",
        "away_team": "Sydney FC",
        "kickoff_utc": datetime(2026, 7, 29, 9, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "Tottenham Hotspur",
        "kickoff_utc": datetime(2026, 8, 1, 9, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Tottenham Hotspur",
        "away_team": "Getafe",
        "kickoff_utc": datetime(
            2026, 8, 8, 14, 0, tzinfo=timezone.utc
        ),  # 3pm BST = 2pm UTC, behind closed doors
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Tottenham Hotspur",
        "away_team": "Hoffenheim",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Tottenham Hotspur",
        "away_team": "Hoffenheim",
        "kickoff_utc": datetime(
            2026, 8, 16, 11, 0, tzinfo=timezone.utc
        ),  # 12pm BST = 11am UTC, behind closed doors
        "competition_name": "Pre-Season Friendly",
    },
    # === SERIE A FIXTURES ===
    # Source: Pazzidifanta, Sekbernews, OneFootball [citation:2][citation:6][citation:10]
    # AC Milan
    {
        "home_team": "Celtic",
        "away_team": "AC Milan",
        "kickoff_utc": datetime(
            2026, 7, 25, 15, 0, tzinfo=timezone.utc
        ),  # 5pm CEST = 3pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "AC Milan",
        "away_team": "Inter Milan",
        "kickoff_utc": datetime(
            2026, 8, 5, 0, 0, tzinfo=timezone.utc
        ),  # Perth, time TBC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester United",
        "away_team": "AC Milan",
        "kickoff_utc": datetime(2026, 8, 15, 14, 45, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Bologna
    {
        "home_team": "Bologna",
        "away_team": "Iraklis",
        "kickoff_utc": datetime(
            2026, 7, 25, 14, 0, tzinfo=timezone.utc
        ),  # 4pm CEST = 2pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Brighton",
        "away_team": "Bologna",
        "kickoff_utc": datetime(2026, 8, 15, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Como
    {
        "home_team": "Arsenal",
        "away_team": "Como",
        "kickoff_utc": datetime(2026, 8, 12, 18, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Liverpool",
        "away_team": "Como",
        "kickoff_utc": datetime(2026, 8, 16, 17, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Fiorentina
    {
        "home_team": "Queens Park Rangers",
        "away_team": "Fiorentina",
        "kickoff_utc": datetime(2026, 7, 25, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Genoa
    {
        "home_team": "Genoa",
        "away_team": "Vicenza",
        "kickoff_utc": datetime(
            2026, 7, 25, 15, 0, tzinfo=timezone.utc
        ),  # 5pm CEST = 3pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Bournemouth",
        "away_team": "Genoa",
        "kickoff_utc": datetime(2026, 8, 4, 0, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Inter Milan [citation:2][citation:6]
    {
        "home_team": "Karlsruher",
        "away_team": "Inter Milan",
        "kickoff_utc": datetime(2026, 7, 26, 0, 0, tzinfo=timezone.utc),  # time TBC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Manchester City",
        "away_team": "Inter Milan",
        "kickoff_utc": datetime(2026, 8, 1, 11, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "AC Milan",
        "away_team": "Inter Milan",
        "kickoff_utc": datetime(2026, 8, 5, 0, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Juventus",
        "away_team": "Inter Milan",
        "kickoff_utc": datetime(
            2026, 8, 8, 0, 0, tzinfo=timezone.utc
        ),  # Perth, time TBC
        "competition_name": "Pre-Season Friendly",
    },
    # Juventus [citation:2][citation:6][citation:10]
    {
        "home_team": "Standard Liege",
        "away_team": "Juventus",
        "kickoff_utc": datetime(
            2026, 7, 25, 18, 0, tzinfo=timezone.utc
        ),  # 8pm CEST = 6pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Chelsea",
        "away_team": "Juventus",
        "kickoff_utc": datetime(2026, 8, 5, 11, 30, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    {
        "home_team": "Juventus",
        "away_team": "Inter Milan",
        "kickoff_utc": datetime(2026, 8, 8, 0, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Lecce
    {
        "home_team": "Lecce",
        "away_team": "NK Istra",
        "kickoff_utc": datetime(
            2026, 7, 25, 15, 30, tzinfo=timezone.utc
        ),  # 5:30pm CEST = 3:30pm UTC
        "competition_name": "Pre-Season Friendly",
    },
    # Parma
    {
        "home_team": "Trento",
        "away_team": "Parma",
        "kickoff_utc": datetime(
            2026, 7, 25, 16, 0, tzinfo=timezone.utc
        ),  # 6pm CEST = 4pm UTC, 45-min match
        "competition_name": "Pre-Season Friendly",
    },
    # Roma
    {
        "home_team": "Brighton",
        "away_team": "Roma",
        "kickoff_utc": datetime(2026, 8, 8, 14, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Sassuolo
    {
        "home_team": "Trento",
        "away_team": "Sassuolo",
        "kickoff_utc": datetime(
            2026, 7, 25, 16, 0, tzinfo=timezone.utc
        ),  # 45-min match
        "competition_name": "Pre-Season Friendly",
    },
    # Torino
    {
        "home_team": "Torino",
        "away_team": "Cittadella",
        "kickoff_utc": datetime(2026, 7, 25, 15, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
    # Udinese
    {
        "home_team": "Udinese",
        "away_team": "Nottingham Forest",
        "kickoff_utc": datetime(2026, 8, 8, 18, 0, tzinfo=timezone.utc),
        "competition_name": "Pre-Season Friendly",
    },
]
