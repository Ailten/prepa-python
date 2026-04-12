from classPy.LivingEntity import LivingEntity
from classPy.Fight import Fight

#from classPy.DBConnect import DBConnect
#print(DBConnect.callToDB('SELECT * FROM class'))

myCharacter = LivingEntity('Iop')
myOponent = LivingEntity('Abra')

Fight.duel(myCharacter, myOponent, turnWait=0.6)



# TODO :
# make spellsDetails take a range random for damage (and heal).
# a class for other type of livingEntity (child).
# set SQL DB, for livingEntity stats, pseudo adventurer, ... etc.