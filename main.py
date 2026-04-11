from classPy.LivingEntity import LivingEntity
from classPy.Fight import Fight

#from classPy.DBConnect import DBConnect
#print(DBConnect.callToDB('SELECT * FROM class'))

myCharacter = LivingEntity('Iop')
myOponent = LivingEntity('Abra')

Fight.duel(myCharacter, myOponent, turnWait=0.6)



# TODO :
# a class for other type of livingEntity (child).
# - with spell dedicate and override of logic turn.
# --- add spell param (turn cooldown, last time launched, isCooldownFree()).
# set SQL DB, for livingEntity stats, pseudo adventurer, ... etc.