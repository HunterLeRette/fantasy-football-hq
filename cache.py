import json
import os
from datetime import datetime, timedelta

CACHE_FILE = "cache/players_cache.json"
CACHE_TTL_HOURS = 24

# Check cache file to see if it's been loaded later than CACHE_TTL_HOURS
def _is_cache_fresh():
    if not os.path.exists(CACHE_FILE):
        return False
    with open(CACHE_FILE, "r") as f:
        data = json.load(f)  # Holds dict of players
    fetched_at = datetime.fromisoformat(data["fetched_at"])
    return datetime.now() - fetched_at < timedelta(hours=CACHE_TTL_HOURS)


# Update cache file with modern data
def _refresh_cache(sleeper_service):
    players = sleeper_service.get_all_players()
    os.makedirs("cache", exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump({"fetched_at": datetime.now().isoformat(), "players": players}, f)
    return players


# Get Cached Players
def get_cached_players(sleeper_service):
    if _is_cache_fresh():
        with open(CACHE_FILE, "r") as f:
            return json.load(f)["players"]
    return _refresh_cache(sleeper_service)


