from classPy.LivingEntity import LivingEntity
from classPy.Spell import Spell
from classPy.Elements import Elements

class Healer(LivingEntity):
    def __init__(self, name='Healer', lvl=1):
        super().__init__(name)
        self.lvl = lvl
        self.spells = {
            'rafale': Spell.initDetails(
                value=2,
                rangValue=4,
                element=int(Elements.AIR),
                name='rafale'
            ),
            'premier soin': Spell.initDetails(
                value=8,
                rangValue=3,
                element=int(Elements.FIRE),
                name='premier soin',
                cooldown=1
            ),
            'porte bonheur': Spell.initDetails(
                value=4,
                element=int(Elements.AIR),
                name='porte bonheur',
                cooldown=6,
                lvl=2
            ),
            'boule de feu': Spell.initDetails(
                value=6,
                rangValue=3,
                element=int(Elements.FIRE),
                name='boule de feu',
                cooldown=1,
                lvl=3
            ),
            'drain vitale': Spell.initDetails(
                value=6,
                rangValue=2,
                isSteelHP=True,
                element=int(Elements.WATER),
                name='drain vitale',
                cooldown=1,
                lvl=4
            ),
            'régenération majeur': Spell.initDetails(
                value=40,
                element=int(Elements.FIRE),
                name='régenération majeur',
                cooldown=8,
                lvl=5
            )
        }

    def playTurn(self, oponent) -> str:

        # debuff.
        if(self.spells['porte bonheur'].turnUntilReDo == 3):
            self.dmg[self.spells['porte bonheur'].element] -= self.spells['puissance'].value
            print(f'{self.name} perd porte bonheur.')

        # pick spell.
        if(self.spells['drain vitale'].isCanBePlay(self.lvl) and self.dmgPurcent[int(Elements.WATER)] >= self.dmgPurcent[int(Elements.FIRE)]):
            self.spells['drain vitale'].resetCooldown()
            return self.atkOponent(oponent, self.spells['drain vitale'].clone())
        elif(self.spells['régenération majeur'].isCanBePlay(self.lvl) and self.HP.getPurcent() < 0.15):
            self.spells['régenération majeur'].resetCooldown()
            return self.selfHeal(self.spells['régenération majeur'].clone())
        elif(self.spells['porte bonheur'].isCanBePlay(self.lvl) and self.HP.getPurcent() < 0.8):
        elif(self.spells['premier soin'].isCanBePlay(self.lvl) and self.HP.getPurcent() < 0.8):
            self.spells['premier soin'].resetCooldown()
            return self.selfHeal(self.spells['premier soin'].clone())
        elif(self.spells['boule de feu'].isCanBePlay(self.lvl) and self.dmgPurcent[int(Elements.FIRE)] >= self.dmgPurcent[int(Elements.AIR)]):
            self.spells['boule de feu'].resetCooldown()
            return self.atkOponent(oponent, self.spells['boule de feu'].clone())
        return self.atkOponent(oponent, self.spells['rafale'].clone())