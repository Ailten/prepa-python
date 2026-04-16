from classPy.LivingEntity import LivingEntity

class Abra(LivingEntity):
    def __init__(self):
        super().__init__('Abra')
        self.lvl = 2
        self.spells = {
            'fouet racine': Spell.initDetails(
                value=6,
                rangValue=4,
                element=int(Elements.EARTH),
                name='fouet racine'
            ),
            'drain': Spell.initDetails(
                value=10,
                rangValue=2,
                isSteelHP=True,
                element=int(Elements.WATER),
                name='drain',
                cooldown=3
            ),
            'bourgeon neuf': Spell.initDetails(
                value=2,
                element=int(Elements.EARTH),
                name='bourgeon neuf',
                cooldown=6
            )
        }

    def playTurn(self, oponent) -> str:

        # debuff.
        if(self.spells['bourgeon neuf'].turnUntilReDo == 2):
            self.dmg[self.spells['bourgeon neuf'].element] -= self.spells['bourgeon neuf'].value
            print(f'{self.name} perd bourgeon neuf.')
        
        # pick spell.
        if(self.spells['drain'].isCanBePlay(self.lvl) and self.HP.getPurcent <= 0.5):
            self.spells['drain'].resetCooldown()
            return self.selfBoostResAllElements(self.spells['drain'].clone())
        elif(self.spells['bourgeon neuf'].isCanBePlay(self.lvl) and self.HP.getPurcent >= 0.9):
            self.spells['bourgeon neuf'].resetCooldown()
            return self.selfBoostDamage(self.spells['bourgeon neuf'].clone())
        return self.atkOponent(oponent, self.spells['fouet racine'].clone())



