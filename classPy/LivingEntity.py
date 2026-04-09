from classPy.Jauge import Jauge
from classPy.Spell import Spell
import math
import random

class LivingEntity():

    def __init__(self, name: str):
        self.name = name

        self.HP = Jauge(100)  # Heal Point.
        self.MP = Jauge(100)  # Mana Point.
        self.SP = Jauge(100)  # Stamina Point.

        self.res = [0,0,0,0]  # stats.
        self.dmg = [0,0,0,0]
        self.resPurcent = [0.0,0.0,0.0,0.0]
        self.dmgPurcent = [0.0,0.0,0.0,0.0]
        self.crit = Jauge.initWithValue(0, 99)
        self.parade = Jauge.initWithValue(0, 99)
        self.dmgCrit = 0
        self.resCrit = 0


    def playTurn(self, oponent) -> str:
        return self.atkOponent(oponent)

    def atkOponent(self, oponent) -> str:

        spell = self.pickAtk().clone()
        self.calcDamage(spell)
        oponent.calcRes(spell)
        oponent.takeHit(spell)

        return f'{self.name} attaque {oponent.name}, ({spell.value} damages), {oponent.HP.currentValue} HP restant.'

    def pickAtk(self):
        damage = 0
        for i in range(3):
            damage += self.rngDice(6)
        element = self.rng(4)
        return Spell(damage, element)

    def calcDamage(self, spell: Spell):
        spell.value *= 1.0 + self.dmgPurcent[spell.element]
        spell.value += self.dmg[spell.element]
        if(self.rng(100) <= self.crit.currentValue):
            spell.value += self.dmgCrit[spell.element]
            spell.value *= 1.20
            spell.isCrit = True

    def calcRes(self, spell: Spell):
        spell.value -= self.res[spell.element]
        spell.value *= 1.0 - self.resPurcent[spell.element]
        if(self.rng(100) <= self.parade.currentValue):
            spell.value *= 0.8
            spell.isParade = True
        if(spell.isCrit):
            spell.value -= self.resCrit

    def takeHit(self, spell: Spell):
        self.HP.decreate(spell.value)

    
    def isDead(self) -> bool:
        return self.HP.isEmpty()
        

    def rng(self, maxValueExclude) -> int:  # from zero to num send (-1).
        return math.floor(random.random() * maxValueExclude)
    def rngDice(self, faces=6) -> int:  # from one to num send.
        return self.rng(faces) + 1