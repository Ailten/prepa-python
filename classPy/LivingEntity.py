from classPy.Jauge import Jauge
import math
import random

class LivingEntity():

    def __init__(self, name):
        self.name = name

        self.HP = Jauge(100)  # Heal Point.
        self.MP = Jauge(100)  # Mana Point.
        self.SP = Jauge(100)  # Stamina Point.


    def atkOponent(self, oponent) -> str:
        log = f'{self.name} attaque {oponent.name},'
        damage = self.calcAtk()
        damage = oponent.calcRes(damage)
        log += f' ({damage} damages),'
        log += f' {oponent.HP.currentValue} HP restant.'
        oponent.takeHit(damage)
        return log

    def calcAtk(self):
        damage = 0
        for i in range(3):
            damage += self.D6()
        return damage
    
    def calcRes(self, damage):
        return damage

    def takeHit(self, damage):
        self.HP.decreate(damage)

    
    def isDead(self) -> bool:
        return self.HP.isEmpty()
        

    def D6(self, faces=6) -> int:
        return math.ceil(random.random() * faces)