from dataclasses import dataclass
from models.player import Player
from models.stat_mixins import PassingStatsMixin, RushingStatsMixin, ReceivingStatsMixin

# Class to initialize the Quarterback position using proper Passing and Rushing mixins
@dataclass
class QB(Player, PassingStatsMixin, RushingStatsMixin):
    pass

# Class to initialize the Running Back position using proper Rushing and Receiving mixins
@dataclass
class RB(Player, RushingStatsMixin, ReceivingStatsMixin):
    pass

# Class to initialize the Wide Receiver position using proper Receiving mixin
@dataclass
class WR(Player, ReceivingStatsMixin):
    pass

# Class to initialize the Tight End position using proper Receiving mixin
@dataclass
class TE(Player, ReceivingStatsMixin):
    pass
