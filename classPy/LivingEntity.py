from classPy.Jauge import Jauge
from classPy.Spell import Spell
from classPy.RandomManager import RandomManager
from classPy.Elements import Elements
import math

class LivingEntity():
    def __init__(self, name: str):
        self.name = name
        self.lvl = 1

        self.HP = Jauge(60)  # Heal Point.
        #self.MP = Jauge(100)  # Mana Point.
        #self.SP = Jauge(100)  # Stamina Point.

        self.res = [0,0,0,0]  # stats.
        self.dmg = [0,0,0,0]
        self.resPurcent = [0.0,0.0,0.0,0.0]
        self.dmgPurcent = [0.0,0.0,0.0,0.0]
        self.crit = Jauge.initWithValue(0, 100)
        self.parade = Jauge.initWithValue(0, 100)
        self.dmgCrit = 0
        self.resCrit = 0

        self.spells = None

    def updateAllSpell(self):
        if self.spells == None:
            return
        for s in self.spells.values():
            s.updateTurnCooldown()

    def playTurn(self, oponent) -> str:
        return self.atkOponent(oponent, self.pickAtk().clone())

    def atkOponent(self, oponent, spell: 'Spell') -> str:

        self.calcDamage(spell)
        oponent.calcRes(spell)
        spell.value = int(spell.value)
        oponent.takeHit(spell)
        if spell.isSteelHP:  # todo, pritn in lock the steel HP.
            self.takeHeal(int(spell.value / 2))

        critStr = '[CC!]' if spell.isCrit else ''
        parStr = '[Par!]' if spell.isParade else ''
        spellNameStr = f'{self.name} lance {spell.name} !' if spell.name != None else f'{self.name} attaque {oponent.name},'

        return (
            f'{spellNameStr}'+
            f'{critStr}'+
            f' ({spell.value} damages)'+
            f'{parStr}'+
            f', {oponent.HP.currentValue} HP restant.'
        )

    def selfHeal(self, spell: 'Spell') -> str:

        self.calcDamage(spell)
        spell.value = int(spell.value)
        self.takeHeal(spell)

        critStr = '[CC!]' if spell.isCrit else ''
        spellNameStr = f'{self.name} lance {spell.name} !' if spell.name != None else f'{self.name} ce soigne,'

        return (
            f'{spellNameStr}'+
            f'{critStr}'+
            f' ({spell.value} soins)'
        )

    def selfBoostDamage(self, spell: 'Spell') -> str:
        spell.value = int(spell.value)
        self.dmg[spell.element] += spell.value

        spellNameStr = f'{self.name} lance {spell.name} !' if spell.name != None else f'{self.name} ce boost,'
        elementStr = Elements(spell.element).getName()

        return (
            f'{spellNameStr}'+
            f' ({spell.value} domages {elementStr})'
        )

    def pickAtk(self) -> 'Spell':
        damage = RandomManager.rngBetween(4, 6)
        element = RandomManager.rng(4)
        return Spell(damage, element)

    def calcDamage(self, spell: Spell):
        if(spell.rangValue != 0):
            spell.value += RandomManager.rngBetween(0, spell.rangValue)
        spell.value *= 1.0 + self.dmgPurcent[spell.element]
        spell.value += self.dmg[spell.element]
        if(RandomManager.rngDice(100) <= self.crit.currentValue):
            spell.value += self.dmgCrit
            spell.value *= 1.20
            spell.isCrit = True

    def calcHeal(self, spell: Spell):
        self.calcDamage(spell)  # todo: custom calcul for heal.

    def calcRes(self, spell: Spell):
        spell.value -= self.res[spell.element]
        spell.value *= 1.0 - self.resPurcent[spell.element]
        if(RandomManager.rngDice(100) <= self.parade.currentValue):
            spell.value *= 0.8
            spell.isParade = True
        if(spell.isCrit):
            spell.value -= self.resCrit

    def takeHit(self, spell: Spell):
        spell.value = math.max(spell.value, 0)
        self.HP.decreate(spell.value)
        if(self.HP.currentValue <= 0):
            self.die()
        
        if(self.HP.isUnderRange()):
            self.HP.clamp()

    def takeHeal(self, spell: Spell):
        spell.value = math.max(spell.value, 0)
        self.HP.increase(spell.value)

        if(self.HP.isOverRange()):
            self.HP.clamp()

    def die(self, spell: Spell):
        pass

    
    def isDead(self) -> bool:
        return self.HP.isEmpty()
    