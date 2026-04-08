from classPy.LivingEntity import LivingEntity

myCharacter = LivingEntity('Iop')
myOponent = LivingEntity('Abra')

print(f'Fight start : {myCharacter.name} VS {myOponent.name}')

while(True):

    log = myCharacter.atkOponent(myOponent)
    print(log)
    if(myOponent.isDead()):
        print(f'{myOponent.name} est mort.')
        break

    log = myOponent.atkOponent(myCharacter)
    print(log)
    if(myCharacter.isDead()):
        print(f'{myCharacter.name} est mort.')
        break

# TODO :
# a class for fight between livintEntity.
# a class for other type of livingEntity (child).
# set other stats (res, dmg, resPurcent, dmgPurcent, crit, parade, dmgCrit, resCrit).
# set SQL DB, for livingEntity stats, pseudo adventurer, ... etc.