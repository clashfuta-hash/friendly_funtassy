from __future__ import annotations

from typing import Dict, List

# Canonical name (as used in hardcoded_fixtures.py) -> variants 365Scores
# might display it as. Add to this whenever a fixture fails to resolve
# because the stored name doesn't match 365Scores' name field.
TEAM_ALIASES: Dict[str, List[str]] = {
    "Aston Villa": ["Aston Villa", "Villa"],
    "Porto": ["Porto", "FC Porto"],
    "Real Sociedad": ["Real Sociedad", "Sociedad"],
    "Tottenham": ["Tottenham", "Spurs", "Tottenham Hotspur"],
    "Auckland FC": ["Auckland FC", "Auckland"],
    "Sydney FC": ["Sydney FC"],
    "Chelsea": ["Chelsea"],
    "Western Sydney Wanderers": ["Western Sydney Wanderers", "Western Sydney"],
    "Juventus": ["Juventus", "Juve"],
    "Arsenal": ["Arsenal"],
    "Girona": ["Girona", "Girona FC"],
    "Real Betis": ["Real Betis", "Betis"],
    "Manchester City": ["Manchester City", "Man City"],
    "Inter Milan": ["Inter Milan", "Inter", "Internazionale"],
    "AC Milan": ["AC Milan", "Milan"],
    "Bournemouth": ["Bournemouth", "AFC Bournemouth"],
    "Genoa": ["Genoa"],
    "Crystal Palace": ["Crystal Palace", "Palace"],
    "Fulham": ["Fulham"],
    "Brighton": ["Brighton", "Brighton & Hove Albion", "Brighton and Hove Albion"],
    "Roma": ["Roma", "AS Roma"],
    "Brentford": ["Brentford"],
    "Stade Rennais": ["Stade Rennais", "Rennes"],
    "Getafe": ["Getafe", "Getafe CF"],
}


def aliases_for(name: str) -> List[str]:
    return TEAM_ALIASES.get(name, [name])
