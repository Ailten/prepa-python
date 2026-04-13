from enum import IntEnum

class Elements(IntEnum):
    FIRE = 0
    EARTH = 1
    WATER = 2
    AIR = 3

    def getName(self):
        match self:
            case Elements.FIRE:
                return "feu"
            case Elements.EARTH:
                return "terre"
            case Elements.WATER:
                return "eau"
            case Elements.AIR:
                return "air"