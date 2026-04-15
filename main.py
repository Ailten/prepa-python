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
myCharacter = Tank('Daramu Nico', lvl=1)
myOponent = LivingEntity('Abra')

Fight.duel(myCharacter, myOponent, turnWait=0.6)



# TODO :
# shild on a specific element is a probleme (when ennemey atk in 4 element).
# --> make it add res in all elem, and retire in all elem.
# --> same for damage boost.
# a class for other type of livingEntity (child).
# set SQL DB, for livingEntity stats, pseudo adventurer, ... etc.