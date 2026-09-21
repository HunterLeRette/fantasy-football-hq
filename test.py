import requests
import pandas as pd
from connectors.service_layer import SleeperService
from storage.cache import get_cached_players
import time
import nflreadpy as nfl



data = nfl.load_player_stats(seasons=[2026])
all_columns = data.columns

# Group columns by keyword
categories = {
    "Passing": [c for c in all_columns if "pass" in c],
    "Rushing": [c for c in all_columns if "rush" in c or c == "carries"],
    "Receiving": [c for c in all_columns if "rec" in c or c in ("targets", "air_yards_share", "wopr", "racr")],
    "Kicking": [c for c in all_columns if "fg" in c or "pat" in c or "gwfg" in c],
    "Defense": [c for c in all_columns if c.startswith("def_")],
    "Special Teams": [c for c in all_columns if "punt" in c or "kickoff" in c or c.startswith("pt_")],
    "Fumbles": [c for c in all_columns if "fumble" in c],
}

# Track columns already categorized so we can show what's left over
categorized = set()
for cols in categories.values():
    categorized.update(cols)

categories["Other / Identifiers"] = [c for c in all_columns if c not in categorized]

# Print nicely
for category, cols in categories.items():
    print(f"\n{'=' * 50}")
    print(f"{category} ({len(cols)} columns)")
    print('=' * 50)
    for col in cols:
        print(f"  - {col}")

