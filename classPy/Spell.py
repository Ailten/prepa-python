
class Spell():
    def __init__(self, value: int, element: int):
        self.value = value
        self.element = element
        self.isCrit = False
        self.isParade = False
        self.cooldown = 0
        self.turnUntilReDo = 0
        self.name = None

    @classmethod
    def initDetails(self, value: int, element: int, cooldown=0, name='attaque', lvl=1):
        instance = Spell(value, element)
        instance.cooldown = cooldown
        instance.turnUntilReDo = 0
        instance.name = name
        return instance

    def clone(self) -> 'Spell':
        instance = Spell(self.value, self.element)
        instance.isCrit = self.isCrit
        instance.isParade = self.isParade
        instance.cooldown = self.cooldown
        instance.turnUntilReDo = self.turnUntilReDo
        instance.name = self.name
        return instance
        
    def isCanBePlay(self) -> bool:
        return self.turnUntilReDo <= 0

    def resetCooldown(self):
        self.turnUntilReDo = self.cooldown
    def updateTurnCooldown(self):
        if(self.turnUntilReDo > 0):
            self.turnUntilReDo -= 1