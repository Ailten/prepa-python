from classPy.LivingEntity import LivingEntity
from classPy.Spell import Spell
from classPy.Element import Element

class Iop(LivingEntity):
    def __init__(self, name='Iop', lvl=1):
        super().__init__(name)
        self.lvl = lvl
        self.spells = {
            Spell.initDetails(
                value=4,
                rangValue=2,
                element=Element.EARTH,
                name='pression'
            ),
            Spell.initDetails(
                value=2,
                element=Element.EARTH,
                name='puissance',
                cooldown=4,
                lvl=2
            )
            Spell.initDetails(
                value=12,
                rangValue=3,
                element=Element.FIRE,
                name='vitalité',
                cooldown=5,
                lvl=3
            ),
            Spell.initDetails(
                value=20,
                rangValue=5,
                element=Element.EARTH,
                name='colère de iop',
                cooldown=8,
                lvl=5
            )
        }
    
    def playTurn(self, oponent) -> str:

        # debuff.
        if(self.spells['puissance'].cooldown == 1):
            self.dmg[self.spells['puissance'].element] -= self.spells['puissance'].value

        # pick spell.
        if(self.spells['colère de iop'].isCanBePlay(self.lvl)):
            self.spells['colère de iop'].value *= 2
            self.spells['colère de iop'].resetCooldown()
            return self.atkOponent(oponent, self.spells['colère de iop'].clone())
        elif(self.spells['puissance'].isCanBePlay(self.lvl) and self.HP.getPurcent() > 0.8):
            self.spells['puissance'].resetCooldown()
            return self.selfBoostDamage(self.spells['puissance'].clone())
        elif(self.spells['vitalité'].isCanBePlay(self.lvl) and self.HP.getPurcent() < 0.2):
            self.spells['vitalité'].resetCooldown()
            return self.selfHeal(self.spells['vitalité'].clone())
        return self.atkOponent(oponent, self.spells['pression'].clone())
