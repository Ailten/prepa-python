from classPy.LivingEntity import LivingEntity

class Rokaille(LivingEntity):
    def __init__(self):
        super().__init__('Rokaille')
        self.lvl = 2
        self.spells = {
            'caillasse': Spell.initDetails(
                value=5,
                rangValue=2,
                element=int(Elements.EARTH),
                name='caillasse'
            ),
            'armure rockailleuse': Spell.initDetails(
                value=1,
                element=int(Elements.EARTH),
                name='armure rockailleuse',
                cooldown=2
            )
        }

    def playTurn(self, oponent) -> str:

        # debuff.
        if(self.spells['armure rockailleuse'].turnUntilReDo == 1):
            pass
        
        # pick spell.
        if(self.spells['armure rockailleuse'].isCanBePlay(self.lvl) and self.HP.getPurcent >= 0.4):
            self.spells['armure rockailleuse'].resetCooldown()
            return self.selfBoostResAllElements(self.spells['armure rockailleuse'].clone())
        return self.atkOponent(oponent, self.spells['caillasse'].clone())



