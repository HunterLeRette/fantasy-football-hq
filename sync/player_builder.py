from models.positions import QB, RB, WR, TE
from models.player import Player

# Maps the sleeper postion strings to the corresponding position classes
POSITION_MAP = {
    'QB': QB,
    'RB': RB,
    'WR': WR,
    'TE': TE
}

# Default Passing Attributes
PASSING_DEFAULTS = {
    "completions": 0,
    "attempts": 0,
    "passing_yards": 0,
    "passing_tds": 0,
    "passing_interceptions": 0,
    "passing_air_yards": 0,
    "passing_epa": 0.0,
    "passing_cpoe": 0.0,
    "pacr": 0.0,
}

# Default Rushing Attributes
RUSHING_DEFAULTS = {
    "carries": 0,
    "rushing_yards": 0,
    "rushing_tds": 0,
    "rushing_epa": 0.0,
    "rushing_10": 0,
    "rushing_12": 0,
    "rushing_20": 0,
    "rushing_40": 0,
}

# Default Receving Attributes
RECEIVING_DEFAULTS = {
    "receptions": 0,
    "targets": 0,
    "receiving_yards": 0,
    "receiving_tds": 0,
    "receiving_air_yards": 0,
    "receiving_yards_after_catch": 0,
    "receiving_epa": 0.0,
    "target_share": 0.0,
    "receiving_10": 0,
    "receiving_16": 0,
    "receiving_20": 0,
    "receiving_40": 0,
    "racr": 0.0,
    "air_yards_share": 0.0,
    "wopr": 0.0,
}

# Combines default mixin dicts that each position needs
POSITION_DEFAULTS = {
    "QB": {**PASSING_DEFAULTS, **RUSHING_DEFAULTS},
    "RB": {**RUSHING_DEFAULTS, **RECEIVING_DEFAULTS},
    "WR": {**RECEIVING_DEFAULTS},
    "TE": {**RECEIVING_DEFAULTS},
}

def build_player(raw_data: dict):
    position = raw_data.get("position")
    player_class = POSITION_MAP.get(position)

    if player_class is None:
        pass  # Add kicker and defense/special team logic later

    # Populate Player with sleeper base player data
    base_fields = {
        'player_id': raw_data.get('player_id'),
        'gsis_id': raw_data.get('gsis_id'),
        'name': f"{raw_data.get('first_name')} {raw_data.get('last_name')}",
        'team': raw_data.get('team'),
        'position': raw_data.get('position'),
        'bye_week': None,  # TODO Sort through matchups to determine bye weeks
        'injury_status': raw_data.get('injury_status'),
    }
    # Position specific mixin statistics defaulted to 0 until updated later
    stats_defaults = POSITION_DEFAULTS[position]

    return player_class(**base_fields, **stats_defaults)
    





    return Player()


