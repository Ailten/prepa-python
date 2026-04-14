from enum import IntEnum

# wip.

class StatusEffect():
    def __init__(self, name: str, turns: int, procWhen: 'ProcWhen', action, target, launcher):
        self.name = name
        self.turns = turns
        self.procWhen = procWhen
        self.action = action  # lambda call when procWhen.
        self.target = target
        self.lancher = launcher


class ProcWhen(IntEnum):
    updateAllSpell = 0
    playTurn = 1
    atkOponent = 2
    selfHeal = 3
    takeHit = 4
    takeHeal = 5
    die = 6