from classPy.LivingEntity import LivingEntity
from classPy.Spell import Spell
from classPy.Elements import Elements

class Iop(LivingEntity):
    def __init__(self, name='Iop', lvl=1):
        super().__init__(name)
        self.lvl = lvl
        self.spells = {
            'pression': Spell.initDetails(
                value=4,
                rangValue=2,
                element=int(Elements.EARTH),
                name='pression'
            ),
            'puissance': Spell.initDetails(
                value=3,
                element=int(Elements.EARTH),
                name='puissance',
                cooldown=4,
                lvl=2
            ),
            'vitalité': Spell.initDetails(
                value=12,
                rangValue=3,
                element=int(Elements.FIRE),
                name='vitalité',
                cooldown=5,
                lvl=3
            ),
            'épée de iop': Spell.initDetails(
                value=5,
                rangValue=3,
                element=int(Elements.EARTH),
                name='épée de iop',
                cooldown=2,
                lvl=4
            ),
            'colère de iop': Spell.initDetails(
                value=20,
                rangValue=5,
                element=int(Elements.EARTH),
                name='colère de iop',
                cooldown=8,
                lvl=5
            )
        }
    
    def playTurn(self, oponent) -> str:

        # debuff.
        if(self.spells['puissance'].turnUntilReDo == 1):
            self.dmg[self.spells['puissance'].element] -= self.spells['puissance'].value
            print(f'{self.name} perd puissance.')

        # pick spell.
        if(self.spells['colère de iop'].isCanBePlay(self.lvl)):
            self.spells['colère de iop'].resetCooldown()
            instance = self.spells['colère de iop'].clone()
            self.spells['colère de iop'].value *= 2
            return self.atkOponent(oponent, instance)
        elif(self.spells['puissance'].isCanBePlay(self.lvl) and self.HP.getPurcent() > 0.8):
            self.spells['puissance'].resetCooldown()
            return self.selfBoostDamage(self.spells['puissance'].clone())
        elif(self.spells['vitalité'].isCanBePlay(self.lvl) and self.HP.getPurcent() < 0.2):
            self.spells['vitalité'].resetCooldown()
            return self.selfHeal(self.spells['vitalité'].clone())
        elif(self.spells['épée de iop'].isCanBePlay(self.lvl)):
            self.spells['épée de iop'].resetCooldown()
            return self.atkOponent(oponent, self.spells['épée de iop'].clone())
        return self.atkOponent(oponent, self.spells['pression'].clone())
