from dataclasses import dataclass

@dataclass
class Player():
    player_id: str
    gsis_id: str | None
    name: str
    team: str
    position: str
    bye_week: int | None
    injury_status: str | None 
    fantasy_points: float
    fantasy_points_ppr: float

