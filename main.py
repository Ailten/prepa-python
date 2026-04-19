from classPy.LivingEntity import LivingEntity
from classPy.Fight import Fight

#from classPy.DBConnect import DBConnect
#print(DBConnect.callToDB('SELECT * FROM class'))

#myCharacter = LivingEntity('Iop')
#myOponent = LivingEntity('Abra')

#from classPy.Adventurer.Mercenaire import Mercenaire
#myCharacter = Mercenaire('Valli Nuavé', lvl=4)
#myOponent = LivingEntity('Abra')

#from classPy.Adventurer.Healer import Healer
#myCharacter = Healer('Assi Ten', lvl=4)
#myOponent = LivingEntity('Abra')

from classPy.Adventurer.Tank import Tank
myCharacter = Tank('Daramu Nino', lvl=4)
myOponent = LivingEntity('Abra')

Fight.duel(myCharacter, myOponent, turnWait=0.6)



# TODO :
# a class for other type of livingEntity (child), mobs.
# set SQL DB, for livingEntity stats, pseudo adventurer, ... etc.
# need a bether way to apply effect with spell (allow to apply effect, with time-turn), (allow to apply many effect in on spell, in many elements), (bether cooldown spell and restriction)...