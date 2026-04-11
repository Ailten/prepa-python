from classPy.Jauge import Jauge
from classPy.Spell import Spell
from classPy.RandomManager import RandomManager
import math

class LivingEntity():

    def __init__(self, name: str):
        self.name = name
        self.lvl = 1

        self.HP = Jauge(100)  # Heal Point.
        self.MP = Jauge(100)  # Mana Point.
        self.SP = Jauge(100)  # Stamina Point.

        self.res = [0,0,0,0]  # stats.
        self.dmg = [0,0,0,0]
        self.resPurcent = [0.0,0.0,0.0,0.0]
        self.dmgPurcent = [0.0,0.0,0.0,0.0]
        self.crit = Jauge.initWithValue(0, 100)
        self.parade = Jauge.initWithValue(0, 100)
        self.dmgCrit = 0
        self.resCrit = 0


    def playTurn(self, oponent) -> str:
        return self.atkOponent(oponent)

    def atkOponent(self, oponent) -> str:

        spell = self.pickAtk().clone()
        self.calcDamage(spell)
        oponent.calcRes(spell)
        spell.value = int(spell.value)
        oponent.takeHit(spell)

        critStr = '[CC!]' if spell.isCrit else ''
        parStr = '[Par!]' if spell.isParade else ''

        return (
            f'{self.name} attaque {oponent.name},'+
            f'{critStr}'+
            f' ({spell.value} damages)'+
            f'{parStr}'+
            f', {oponent.HP.currentValue} HP restant.'
        )

    def pickAtk(self) -> 'Spell':
        damage = RandomManager.rngBetween(6, 12)
        element = RandomManager.rng(4)
        return Spell(damage, element)

    def calcDamage(self, spell: Spell):
        spell.value *= 1.0 + self.dmgPurcent[spell.element]
        spell.value += self.dmg[spell.element]
        if(RandomManager.rngDice(100) <= self.crit.currentValue):
            spell.value += self.dmgCrit
            spell.value *= 1.20
            spell.isCrit = True

    def calcRes(self, spell: Spell):
        spell.value -= self.res[spell.element]
        spell.value *= 1.0 - self.resPurcent[spell.element]
        if(RandomManager.rngDice(100) <= self.parade.currentValue):
            spell.value *= 0.8
            spell.isParade = True
        if(spell.isCrit):
            spell.value -= self.resCrit

    def takeHit(self, spell: Spell):
        self.HP.decreate(spell.value)

    
    def isDead(self) -> bool:
        return self.HP.isEmpty()
    