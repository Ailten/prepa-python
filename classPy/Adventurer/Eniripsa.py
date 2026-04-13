from classPy.LivingEntity import LivingEntity
from classPy.Elements import Elements

class Eniripsa(LivingEntity):
    def __init__(self, name='Eni', lvl=1):
        super().__init__(name)
        self.lvl = lvl
        self.spells = {
            'mot blessant': Spell.initDetails(
                value=2,
                rangValue=4,
                element=int(Elements.AIR),
                name='mot blessant'
            ),
            'mot curatif': Spell.initDetails(
                value=8,
                rangValue=3,
                element=int(Elements.FIRE),
                name='mot curatif',
                cooldown=1
            ),
            'mot préventif': Spell.initDetails(
                value=4,
                element=int(Elements.AIR),
                name='mot préventif',
                cooldown=6,
                lvl=2
            ),
            'mot interdit': Spell.initDetails(
                value=6,
                rangValue=3,
                element=int(Elements.FIRE),
                name='mot interdit',
                cooldown=1,
                lvl=3
            ),
            'mot vampirique': Spell.initDetails(
                value=8,
                rangValue=2,
                element=int(Elements.WATER),
                name='mot vampirique',
                cooldown=1,
                lvl=4,
                isSteelHP=True
            ),
            'mot reconstituant': Spell.initDetails(
                value=40,
                element=int(Elements.FIRE),
                name='mot reconstituant',
                cooldown=8,
                lvl=5
            ),


        }

    def playTurn(self, oponent) -> str:

        # debuff.
        if(self.spells['mot préventif'].turnUntilReDo == 3):
            self.dmg[self.spells['mot préventif'].element] -= self.spells['puissance'].value
            print(f'{self.name} perd mot préventif.')

        # pick spell.
        if(self.spells['mot vampirique'].isCanBePlay(self.lvl) and self.dmgPurcent[int(Elements.WATER)] > self.dmgPurcent[int(Elements.FIRE)])
            self.spells['mot vampirique'].resetCooldown()
            return self.atkOponent(oponent, self.spells['mot vampirique'].clone())
        if(self.spells['mot reconstituant'].isCanBePlay(self.lvl) and self.HP.getPurcent() < 0.15):
            self.spells['mot reconstituant'].resetCooldown()
            return self.selfHeal(self.spells['mot reconstituant'].clone())
        if(self.spells['mot curatif'].isCanBePlay(self.lvl) and self.HP.getPurcent() < 0.8):
            self.spells['mot curatif'].resetCooldown()
            return self.selfHeal(self.spells['mot curatif'].clone())
        if(self.spells['mot interdit'].isCanBePlay(self.lvl)):
            self.spells['mot interdit'].resetCooldown()
            return self.atkOponent(oponent, self.spells['mot interdit'].clone())
        return self.atkOponent(oponent, self.spells['mot blessant'].clone())