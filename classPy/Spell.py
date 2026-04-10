
class Spell():
    def __init__(self, value: int, element: int):
        self.value = value
        self.element = element
        self.isCrit = False
        self.isParade = False

    def clone(self) -> 'Spell':
        instance = Spell(self.value, self.element)
        instance.isCrit = self.isCrit
        instance.isParade = self.isParade
        return instance
