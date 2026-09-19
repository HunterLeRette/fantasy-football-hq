# Service Layer to simplify API interactions
import requests

#Temp
CURRENT_SEASON = 2026

class SleeperService:
    BASE_URL = "https://api.sleeper.app/v1"

# Get User
    def get_user(self, username):
        response = requests.get(f"{self.BASE_URL}/user/{username}")
        response.raise_for_status()
        return response.json()
    
    
# Get League
    def get_league(self, league_id):
        response = requests.get(f"{self.BASE_URL}/league/{league_id}")
        response.raise_for_status()
        return response.json()
    

# Get All Leagues for User
    def get_user_leagues(self, user_id, season=CURRENT_SEASON):
        response = requests.get(f"{self.BASE_URL}/user/{user_id}/leagues/nfl/{season}")
        response.raise_for_status()
        return response.json()
    

# Get Rosters in a League
    def get_rosters(self, league_id):
        response = requests.get(f"{self.BASE_URL}/league/{league_id}/rosters")
        response.raise_for_status()
        return response.json()


# Get Users in a League
    def get_league_users(self, league_id):
        response = requests.get(f"{self.BASE_URL}/league/{league_id}/users")
        response.raise_for_status()
        return response.json()
    

# Get Matchups in a League
    def get_matchups(self, league_id, week):
        response = requests.get(f"{self.BASE_URL}/league/{league_id}/matchups/{week}")
        response.raise_for_status()
        return response.json()


# Get Traded Picks
    def get_traded_picks(self, league_id):
        response = requests.get(f"{self.BASE_URL}/league/{league_id}/traded_picks")
        response.raise_for_status()
        return response.json()


# Get NFL State
    def get_nfl_state(self):
        response = requests.get(f"{self.BASE_URL}/state/nfl")
        response.raise_for_status()
        return response.json()
    

# Get Trending Players
    def get_trending_players(self, trend_type, lookback_hours=24, limit=25):
        response = requests.get(f"{self.BASE_URL}/players/nfl/trending/{trend_type}", params={"lookback_hours": lookback_hours, "limit": limit})
        response.raise_for_status()
        return response.json()
    