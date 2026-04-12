
class Spell():
    def __init__(self, value: int, element: int):
        self.value = value
        self.element = element
        self.isCrit = False
        self.isParade = False
        self.cooldown = 0
        self.turnUntilReDo = 0
        self.name = None
        self.lvl = 1
        self.rangValue = 0

    @classmethod
    def initDetails(self, value: int, element: int, cooldown=0, name='attaque', lvl=1, rangValue=0) -> 'Spell':
        instance = Spell(value, element)
        instance.cooldown = cooldown
        instance.turnUntilReDo = 0
        instance.name = name
        instance.lvl = lvl
        instance.rangValue = rangValue
        return instance

    def clone(self) -> 'Spell':
        instance = Spell(self.value, self.element)
        instance.isCrit = self.isCrit
        instance.isParade = self.isParade
        instance.cooldown = self.cooldown
        instance.turnUntilReDo = self.turnUntilReDo
        instance.name = self.name
        instance.lvl = self.lvl
        instance.rangValue = self.rangValue
        return instance
        
    def isCanBePlay(self, lvl: int) -> bool:
        return (
            self.isHasCooldownFor() and
            self.isHasLvlFor(lvl)
        )
    def isHasCooldownFor(self) -> bool:
        return self.turnUntilReDo <= 0
    def isHasLvlFor(self, lvl: int) -> bool:
        return lvl >= self.lvl

    def resetCooldown(self):
        self.turnUntilReDo = self.cooldown
    def updateTurnCooldown(self):
        if(self.turnUntilReDo > 0):
            self.turnUntilReDo -= 1