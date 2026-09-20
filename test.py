import requests
import pandas as pd
from ServiceLayer import SleeperService
from cache import get_cached_players
import time


sleeper = SleeperService()

league_id = "1312141634963509248"

players = get_cached_players(sleeper)

rosters = sleeper.get_rosters(league_id)

users = sleeper.get_league_users(league_id)

user_lookup = {user["user_id"]: user["display_name"] for user in users}

my_username = 'jwbRaiders'
my_user = sleeper.get_user(my_username)
my_user_id = my_user["user_id"]

my_roster = next(r for r in rosters if r["owner_id"] == my_user_id)

owner_name = user_lookup.get(my_roster["owner_id"], "Unknown Owner")
print(f"Team: {owner_name}")
print ("-" * 30)

for player_id in my_roster["players"]:
    player_info = players.get(player_id)
    if player_info: 
        full_name = f"{player_info['first_name']} {player_info['last_name']}"
        position = player_info.get("position", "?")
        print(f"{full_name} ({position})")
    else:
        print(f"Unkown player_id: {player_id}")




