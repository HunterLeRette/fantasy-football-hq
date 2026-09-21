from dataclasses import dataclass

# Mixin for all Passing Statistics
@dataclass
class PassingStatsMixin():
    completions: int
    attempts: int
    passing_yards: int
    passing_tds: int
    passing_interceptions: int
    passing_air_yards: int
    passing_epa: float
    passing_cpoe: float
    pacr: float  # Passing Air Conversion Ratio


# Mixin for all Rushing Statistics
@dataclass
class RushingStatsMixin():
    carries: int
    rushing_yards: int
    rushing_tds: int
    rushing_epa: float
    rushing_10: int
    rushing_12: int
    rushing_20: int
    rushing_40: int


# Mixin for all Receiving Statistics
@dataclass
class ReceivingStatsMixin():
    receptions: int
    targets: int
    receiving_yards: int
    receiving_tds: int
    receiving_air_yards: int
    receiving_yards_after_catch: int
    receiving_epa: float
    target_share: float
    receiving_10: int
    receiving_16: int
    receiving_20: int
    receiving_40: int
    racr: float  # Receiver Air Conversion Ratio
    air_yards_share: float
    wopr: float  # Weighted Opportunity Rating










