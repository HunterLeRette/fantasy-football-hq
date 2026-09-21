import requests
import pandas as pd
from connectors.service_layer import SleeperService
from storage.cache import get_cached_players
import time
import nflreadpy as nfl
from models.player import Player


service = SleeperService()
players = get_cached_players(service)

raw = players["4046"]  # Josh Allen's real Sleeper player_id, or swap for any ID from your roster

test_player = Player(
    player_id=raw["player_id"],
    gsis_id=raw.get("gsis_id"),
    name=f"{raw['first_name']} {raw['last_name']}",
    team=raw["team"],
    position=raw["position"],
    bye_week=raw.get("bye_week"),
    injury_status=raw.get("injury_status"),
    fantasy_points=0.0,        # Sleeper's player endpoint doesn't include this — comes from matchups later
    fantasy_points_ppr=0.0
)

print(test_player)
