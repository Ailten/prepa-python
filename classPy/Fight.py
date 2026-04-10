from classPy.LivingEntity import LivingEntity
import time

class Fight():

    @classmethod
    def duel(self, entityOne: 'LivingEntity', entityTwo: 'LivingEntity', turnWait=2):

        print('----- Fight start -----')
        print(f'{entityOne.name} VS {entityTwo.name}')
        time.sleep(1)

        while(True):
        
            log = entityOne.playTurn(entityTwo)
            print(log)
            if(entityTwo.isDead()):
                print(f'{entityTwo.name} est mort.')
                print(f'{entityOne.name} gagne le combat.')
                break
            time.sleep(turnWait)

            log = entityTwo.playTurn(entityOne)
            print(log)
            if(entityOne.isDead()):
                print(f'{entityOne.name} est mort.')
                print(f'{entityTwo.name} gagne le combat.')
                break
            time.sleep(turnWait)

        print('----- Fight End -----')

