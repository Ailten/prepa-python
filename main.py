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
#myCharacter = Eniripsa('Assi Ten', lvl=4)
#myOponent = LivingEntity('Abra')

from classPy.Adventurer.Tank import Tank
myCharacter = Feca('Daramu Nico', lvl=1)
myOponent = LivingEntity('Abra')

Fight.duel(myCharacter, myOponent, turnWait=0.6)



# TODO :
# a class for other type of livingEntity (child).
# set SQL DB, for livingEntity stats, pseudo adventurer, ... etc.