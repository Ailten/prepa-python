from classPy.LivingEntity import LivingEntity
from classPy.Fight import Fight
from classPy.Adventurer.Iop import Iop

#from classPy.DBConnect import DBConnect
#print(DBConnect.callToDB('SELECT * FROM class'))

#myCharacter = LivingEntity('Iop')
#myOponent = LivingEntity('Abra')

myCharacter = Iop('Vald', lvl=1)
myOponent = LivingEntity('Abra')

Fight.duel(myCharacter, myOponent, turnWait=0.6)



# TODO :
# a class for other type of livingEntity (child).
# set SQL DB, for livingEntity stats, pseudo adventurer, ... etc.