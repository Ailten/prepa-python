from classPy.LivingEntity import LivingEntity
from classPy.Spell import Spell
from classPy.Elements import Elements

class Feca(LivingEntity):
    def __init__(self, name='Feca', lvl=1):
        super().__init__(name)
        self.lvl = lvl
        self.spells = {
            'coup de bouclier': Spell.initDetails(
                value=2,
                rangValue=4,
                element=int(Elements.EARTH),
                name='coup de bouclier'
            ),
            'première défence': Spell.initDetails(
                value=6,
                element=int(Elements.EARTH),
                name='première défence',
                cooldown=4
            ),
            'retourné': Spell.initDetails(
                value=6,
                rangValue=2,
                element=int(Elements.WATER),
                name='retourné',
                cooldown=5,
                lvl=2
            ),
            'défence de secour': Spell.initDetails(
                value=15,
                element=int(Elements.AIR),
                name='défence de secour',
                cooldown=12,
                lvl=3
            ),
            'furie du survivant': Spell.initDetails(
                value=10,
                rangValue=2,
                isSteelHP=True,
                element=int(Elements.FIRE),
                name='furie du survivant',
                cooldown=3,
                lvl=4
            ),
            'défence sereine': Spell.initDetails(
                value=2,
                element=int(Elements.WATER),
                name='défence sereine',
                cooldown=4,
                lvl=5
            )
        }
    
    def playTurn(self, oponent) -> str:

        # debuff.
        if(self.spells['première défence'].turnUntilReDo == 2):
            self.res[self.spells['première défence'].element] -= self.spells['première défence'].value
            print(f'{self.name} perd première défence.')
        if(self.spells['défence de secour'].turnUntilReDo == 9):
            self.res[self.spells['défence de secour'].element] -= self.spells['défence de secour'].value
            print(f'{self.name} perd défence de secour.')
        if(self.spells['défence sereine'].turnUntilReDo == 9):
            pass
        
        # pick spell.
        if(self.spells['défence sereine'].isCanBePlay(self.lvl) and self.HP.getPurcent >= 0.4 and not self.HP.isFull()):
            self.spells['défence de secour'].resetCooldown()
            return self.selfBoostRes(self.spells['défence de secour'].clone())
        elif(self.spells['défence de secour'].isCanBePlay(self.lvl) and self.HP.getPurcent <= 0.3):
            self.spells['défence de secour'].resetCooldown()
            return self.selfBoostRes(self.spells['défence de secour'].clone())
        elif(self.spells['première défence'].isCanBePlay(self.lvl)):
            self.spells['première défence'].resetCooldown()
            return self.selfBoostRes(self.spells['première défence'].clone())
        elif(self.spells['furie du survivant'].isCanBePlay(self.lvl) and self.HP.getPurcent <= 0.1 and self.dmgPurcent[int(Elements.FIRE)] >= self.dmgPurcent[int(Elements.WATER)]):
            self.spells['furie du survivant'].resetCooldown()
            return self.atkOponent(oponent, self.spells['furie du survivant'].clone())
        elif(self.spells['retourné'].isCanBePlay(self.lvl) and self.dmgPurcent[int(Elements.WATER)] >= self.dmgPurcent[int(Elements.EARTH)]):
            self.spells['retourné'].resetCooldown()
            return self.atkOponent(oponent, self.spells['retourné'].clone())
        return self.atkOponent(oponent, self.spells['coup de bouclier'].clone())
