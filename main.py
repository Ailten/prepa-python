from classPy.LivingEntity import LivingEntity
from classPy.Fight import Fight

#from classPy.DBConnect import DBConnect
#print(DBConnect.callToDB('SELECT * FROM class'))

#myCharacter = LivingEntity('Iop')
#myOponent = LivingEntity('Abra')

#from classPy.Adventurer.Iop import Iop
#myCharacter = Iop('Assistant', lvl=4)
#myOponent = LivingEntity('Abra')

#from classPy.Adventurer.Eniripsa import Eniripsa
#myCharacter = Eniripsa('Assistant', lvl=4)
#myOponent = LivingEntity('Abra')

from classPy.Adventurer.Feca import Feca
myCharacter = Feca('Assistant', lvl=1)
myOponent = LivingEntity('Abra')

Fight.duel(myCharacter, myOponent, turnWait=0.6)



# TODO :
# a class for other type of livingEntity (child).
# set SQL DB, for livingEntity stats, pseudo adventurer, ... etc.