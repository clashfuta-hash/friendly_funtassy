from __future__ import annotations

import unicodedata
from typing import Dict, List

# Canonical name (as used in hardcoded_fixtures.py) -> variants 365Scores
# might display it as. Add to this whenever a fixture fails to resolve
# because the stored name doesn't match 365Scores' name field.
#
# Matching itself (see _normalize below, used by resolver.py's
# _name_matches) is accent/diacritic-insensitive, so entries here don't
# need an ASCII-stripped duplicate of themselves (e.g. "Kasımpaşa" already
# matches "Kasimpasa" without a separate alias) -- this dict is only for
# genuinely different display names/nicknames (e.g. "Man Utd" vs
# "Manchester United"), not spelling/character variants.
TEAM_ALIASES: Dict[str, List[str]] = {
    "Aston Villa": ["Aston Villa", "Villa"],
    "Porto": ["Porto", "FC Porto"],
    "Real Sociedad": ["Real Sociedad", "Sociedad"],
    "Tottenham": ["Tottenham", "Spurs", "Tottenham Hotspur"],
    "Tottenham Hotspur": ["Tottenham Hotspur", "Tottenham", "Spurs"],
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
    "Rennes": ["Rennes", "Stade Rennais"],
    "Getafe": ["Getafe", "Getafe CF"],
    # -- added: previously missing (70% of fixtures were falling back to
    # literal-name-only matching before this pass) --
    "Al Ahli": ["Al Ahli", "Al-Ahli", "Al Ahli SFC"],
    "Atletico Madrid": ["Atletico Madrid", "Atlético Madrid", "Atletico"],
    "Augsburg": ["Augsburg", "FC Augsburg"],
    "BG Pathum United": ["BG Pathum United", "Pathum United", "BGPU"],
    "Bayer Leverkusen": ["Bayer Leverkusen", "Leverkusen"],
    "Bayern Munich": ["Bayern Munich", "Bayern München", "Bayern", "FC Bayern"],
    "Bologna": ["Bologna", "Bologna FC"],
    "Borussia Dortmund": ["Borussia Dortmund", "Dortmund", "BVB"],
    "Borussia Monchengladbach": [
        "Borussia Monchengladbach",
        "Borussia Mönchengladbach",
        "Monchengladbach",
        "Mönchengladbach",
        "Gladbach",
    ],
    "Brest": ["Brest", "Stade Brestois"],
    "Bristol City": ["Bristol City"],
    "Como": ["Como", "Como 1907"],
    "Eintracht Frankfurt": ["Eintracht Frankfurt", "Frankfurt"],
    "Everton": ["Everton"],
    "Famalicão": ["Famalicão", "Famalicao", "FC Famalicão"],
    "Freiburg": ["Freiburg", "SC Freiburg"],
    "Hamburg": ["Hamburg", "Hamburger SV", "HSV"],
    "Hoffenheim": ["Hoffenheim", "TSG Hoffenheim"],
    "Hull City": ["Hull City", "Hull"],
    "Indonesia All-Stars": ["Indonesia All-Stars", "Indonesia All Stars"],
    "Ipswich Town": ["Ipswich Town", "Ipswich"],
    "Johor Darul Ta'zim": ["Johor Darul Ta'zim", "Johor Darul Takzim", "JDT"],
    "K-League All-Stars": ["K-League All-Stars", "K League All-Stars", "K-League XI"],
    "Karlsruher": ["Karlsruher", "Karlsruher SC", "KSC"],
    "Kasımpaşa": ["Kasımpaşa", "Kasimpasa"],
    "Le Havre": ["Le Havre", "Le Havre AC"],
    "Leeds United": ["Leeds United", "Leeds"],
    "Lens": ["Lens", "RC Lens"],
    "Lille": ["Lille", "LOSC Lille", "LOSC"],
    "Liverpool": ["Liverpool"],
    "Mainz": ["Mainz", "Mainz 05", "FSV Mainz 05"],
    "Manchester United": ["Manchester United", "Man Utd", "Man United"],
    "Monaco": ["Monaco", "AS Monaco"],
    "Newcastle United": ["Newcastle United", "Newcastle"],
    "Nice": ["Nice", "OGC Nice"],
    "Nottingham Forest": ["Nottingham Forest", "Nott'm Forest", "Forest"],
    "Osasuna": ["Osasuna", "CA Osasuna"],
    "Oxford United": ["Oxford United", "Oxford"],
    "Paris Saint-Germain": ["Paris Saint-Germain", "PSG", "Paris SG"],
    "RB Leipzig": ["RB Leipzig", "Leipzig"],
    "Rayo Vallecano": ["Rayo Vallecano", "Rayo"],
    "Sporting CP": ["Sporting CP", "Sporting Lisbon", "Sporting"],
    "Stoke City": ["Stoke City", "Stoke"],
    "Strasbourg": ["Strasbourg", "RC Strasbourg"],
    "Stuttgart": ["Stuttgart", "VfB Stuttgart"],
    "Sunderland": ["Sunderland", "Sunderland AFC"],
    "Udinese": ["Udinese", "Udinese Calcio"],
    "Union Berlin": ["Union Berlin", "1. FC Union Berlin"],
    "Valencia": ["Valencia", "Valencia CF"],
    "Vitoria de Guimaraes": [
        "Vitoria de Guimaraes",
        "Vitória de Guimarães",
        "Vitoria Guimaraes",
        "Guimaraes",
    ],
    "Wrexham": ["Wrexham", "Wrexham AFC"],
    "Wycombe Wanderers": ["Wycombe Wanderers", "Wycombe"],
    "Çaykur Rizespor": ["Çaykur Rizespor", "Caykur Rizespor", "Rizespor"],
}


def _normalize(text: str) -> str:
    """Strip accents/diacritics and lowercase, so 'Kasımpaşa' and
    'Kasimpasa', or 'Bayern München' and 'Bayern Munich', compare equal
    without needing a hand-written alias for every character variant.
    Genuinely different display names (nicknames, abbreviations) still
    need a real entry in TEAM_ALIASES above -- this only handles
    spelling/character-encoding drift, not naming drift.

    Turkish dotless-i / dotted-I (ı / İ, as in "Kasımpaşa") have no NFKD
    decomposition -- they're independent codepoints, not a base letter
    plus a combining mark -- so the strip-combining-marks pass below
    would leave them untouched (and Python's default .lower() maps
    İ -> i̇, an i plus a combining dot, not a plain "i"). Both are
    special-cased here before the general NFKD pass so "Kasımpaşa" and
    "Kasimpasa" compare equal.

    Whitespace (and '.'/'-' separators) is stripped entirely rather than
    just collapsed. 365Scores sometimes renders multi-word club names
    with no space at all (e.g. "CaykurRizespor" for our "Çaykur
    Rizespor"), which otherwise breaks the substring check in
    _name_matches even though every letter lines up -- "caykur rizespor"
    is not a substring of "caykurrizespor" once one side has a space and
    the other doesn't. Dropping separators on both sides makes the
    comparison robust to that styling difference without needing a
    hand-written alias per affected club.
    """
    text = text.replace("ı", "i").replace("İ", "I")
    decomposed = unicodedata.normalize("NFKD", text)
    stripped = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    lowered = stripped.lower()
    return "".join(ch for ch in lowered if ch not in " .-")


def aliases_for(name: str) -> List[str]:
    return TEAM_ALIASES.get(name, [name])
