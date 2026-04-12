from classPy.LivingEntity import LivingEntity
import time

class Fight():

    @classmethod
    def duel(self, entityOne: 'LivingEntity', entityTwo: 'LivingEntity', turnWait=2):

        print('----- Fight start -----')
        print(f'{entityOne.name} VS {entityTwo.name}')
        time.sleep(1)

        livingTableTurn = [entityOne, entityTwo]
        idTurn = 0

        while(True):

            prota = livingTableTurn[idTurn]  # select entity who play this turn.
            idTurn = (idTurn + 1) % 2
            enta = livingTableTurn[idTurn]
        
            log = prota.playTurn(enta)  # do the action of turn.
            print(log)

            if(Fight.isEndFight(entityOne, entityTwo)):  # verify if one is dead.
                break

            prota.updateAllSpell()  # update cooldown spells.

            time.sleep(turnWait)  # wait dinamic.

        print('----- Fight End -----')

    @classmethod
    def isEndFight(self, entityOne: 'LivingEntity', entityTwo: 'LivingEntity') -> bool:
        if(entityTwo.isDead()):
            print(f'{entityTwo.name} est mort.')
            print(f'{entityOne.name} gagne le combat.')
            return True
        elif(entityOne.isDead()):
            print(f'{entityOne.name} est mort.')
            print(f'{entityTwo.name} gagne le combat.')
            return True
        return False