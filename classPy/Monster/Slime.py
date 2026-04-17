from classPy.LivingEntity import LivingEntity
from classPy.Elements import Elements

class Slime(LivingEntity):
    def __init__(self):
        super().__init__('Slime')
        self.lvl = 2
        self.spells = {
            'gougoute': Spell.initDetails(
                value=1,
                rangValue=6,
                element=int(Elements.WATER),
                name='gougoute'
            ),
            'visquausité': Spell.initDetails(
                value=20,
                element=int(Elements.WATER),
                name='visquausité',
                cooldown=3
            ),
            'englué': Spell.initDetails(
                value=3,
                element=int(Elements.WATER),
                name='englué',
                cooldown=4
            )
        }

    def playTurn(self, oponent) -> str:

        # debuff.
        if(self.spells['visquausité'].turnUntilReDo == 1):
            self.dmg[self.spells['visquausité'].element] -= self.spells['visquausité'].value
            print(f'{self.name} perd visquausité.')
        if(self.spells['englué'].turnUntilReDo == 1):
            pass
        
        # pick spell.
        if(self.spells['englué'].isCanBePlay(self.lvl) and self.HP.getPurcent <= 0.3):
            self.spells['englué'].resetCooldown()
            oponent.res[self.spells['englué'].element] -= self.spells['englué'].value / 100  # TODO: make a function for effects malus (obligator).
            elemStr = Elements(self.spells['englué'].element).getName()
            return f'{self.name} lance englué ! ({self.spells['englué'].value} {elemStr})'
        elif(self.spells['visquausité'].isCanBePlay(self.lvl) and self.HP.getPurcent >= 0.6):
            self.spells['visquausité'].resetCooldown()
            return self.selfBoostDamage(self.spells['visquausité'].clone())
        return self.atkOponent(oponent, self.spells['gougoute'].clone())



