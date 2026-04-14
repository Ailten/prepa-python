from enum import IntEnum

# wip.

class StatusEffect():
    def __init__(self, name: str, turns: int, procWhen: 'ProcWhen', action):
        self.name = name
        self.turns = turns
        self.procWhen = procWhen
        self.action = action


class ProcWhen(IntEnum):
    updateAllSpell = 0
    playTurn = 1
    atkOponent = 2
    selfHeal = 3
    takeHit = 4
    takeHeal = 5
    die = 6