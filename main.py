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
