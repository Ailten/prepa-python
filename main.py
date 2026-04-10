from classPy.LivingEntity import LivingEntity
from classPy.Fight import Fight

myCharacter = LivingEntity('Iop')
myCharacter.crit.currentValue = 20
myOponent = LivingEntity('Abra')

Fight.duel(myCharacter, myOponent, turnWait=0.6)



# TODO :
# a class for other type of livingEntity (child).
# - with spell dedicate and override of logic turn.
# --- add spell param (turn cooldown, last time launched, isCooldownFree()).
# set SQL DB, for livingEntity stats, pseudo adventurer, ... etc.