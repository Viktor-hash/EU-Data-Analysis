from enum import Enum


class Weight(Enum):
    MAX_MORE = 4
    HIGH_MORE = 3
    MEDIUM_MORE = 2
    LOW_MORE = 1
    NEUTRAL = 0
    LOW_LESS = -1
    MEDIUM_LESS = -2
    HIGH_LESS = -3
    MAX_LESS = -4
