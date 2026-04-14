from classPy.LivingEntity import LivingEntity
from classPy.Spell import Spell
from classPy.Elements import Elements

class Iop(LivingEntity):
    def __init__(self, name='Iop', lvl=1):
        super().__init__(name)
        self.lvl = lvl
        self.spells = {
            'estoc': Spell.initDetails(
                value=4,
                rangValue=2,
                element=int(Elements.EARTH),
                name='estoc'
            ),
            'entail': Spell.initDetails(
                value=2,
                rangValue=3,
                element=int(Elements.AIR),
                name='entail'
            ),
            'confiance': Spell.initDetails(
                value=3,
                element=int(Elements.EATH),
                name='confiance',
                cooldown=4,
                lvl=2
            ),
            'fierté': Spell.initDetails(
                value=12,
                rangValue=3,
                element=int(Elements.FIRE),
                name='fierté',
                cooldown=5,
                lvl=3
            ),
            'escrime avencée': Spell.initDetails(
                value=6,
                rangValue=3,
                element=int(Elements.FIRE),
                name='escrime avencée',
                cooldown=1,
                lvl=4
            ),
            'dépassement': Spell.initDetails(
                value=16,
                rangValue=5,
                element=int(Elements.EARTH),
                name='dépassement',
                cooldown=6,
                lvl=5
            )
        }
    
    def playTurn(self, oponent) -> str:

        # debuff.
        if(self.spells['confiance'].turnUntilReDo == 1):
            self.dmg[self.spells['confiance'].element] -= self.spells['confiance'].value
            print(f'{self.name} perd confiance.')
        if(self.spells['fierté'].turnUntilReDo == 1):
            instance = self.spells['fierté'].clone()
            instance.value *= 0.5
            instance.value = int(instance.value)
            self.takeHit(instance)
            print(f'{self.name} perd fierté.')

        # pick spell.
        if(self.spells['dépassement'].isCanBePlay(self.lvl)):
            self.spells['dépassement'].resetCooldown()
            instance = self.spells['dépassement'].clone()
            self.spells['dépassement'].value *= 1.5
            self.spells['dépassement'].value = int(self.spells['dépassement'].value)
            return self.atkOponent(oponent, instance)
        elif(self.spells['confiance'].isCanBePlay(self.lvl) and self.HP.getPurcent() > 0.8):
            self.spells['confiance'].resetCooldown()
            return self.selfBoostDamage(self.spells['confiance'].clone())
        elif(self.spells['fierté'].isCanBePlay(self.lvl) and self.HP.getPurcent() < 0.2):
            self.spells['fierté'].resetCooldown()
            return self.selfHeal(self.spells['fierté'].clone())
        elif(self.spells['escrime avencée'].isCanBePlay(self.lvl) and self.dmgPurcent[int(Elements.FIRE)] >= self.dmgPurcent[int(Elements.AIR)]):
            self.spells['escrime avencée'].resetCooldown()
            return self.atkOponent(oponent, self.spells['escrime avencée'].clone())
        elif(self.spells['entail'].isCanBePlay(self.lvl) and self.dmgPurcent[int(Elements.AIR)] >= self.dmgPurcent[int(Elements.EARTH)]):
            instance = self.spells['entail'].clone()
            self.spells['entail'].value -= 1
            self.spells['entail'].value = math.min(self.spells['entail'].value, 0)
            self.spells['entail'].rangValue += 2
            self.spells['entail'].rangValue = math.min(self.spells['entail'].rangValue, 15)
            return self.atkOponent(oponent, instance)
        return self.atkOponent(oponent, self.spells['estoc'].clone())
