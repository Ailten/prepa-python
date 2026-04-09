from classPy.LivingEntity import LivingEntity
import time

myCharacter = LivingEntity('Iop')
myOponent = LivingEntity('Abra')

print(f'Fight start : {myCharacter.name} VS {myOponent.name}')
time.sleep(1)

while(True):

    log = myCharacter.playTurn(myOponent)
    print(log)
    if(myOponent.isDead()):
        print(f'{myOponent.name} est mort.')
        break
    time.sleep(2)

    log = myOponent.playTurn(myCharacter)
    print(log)
    if(myCharacter.isDead()):
        print(f'{myCharacter.name} est mort.')
        break
    time.sleep(2)



# TODO :
# a class for fight between livintEntity.
# a class for other type of livingEntity (child).
# add spell param (turn cooldown, last time launched, isCooldownFree()).
# set SQL DB, for livingEntity stats, pseudo adventurer, ... etc.