from classPy.Mercenaire import Mercenaire
from classPy.Healer import Healer
from classPy.Tank import Tank

# not use currently.
class AdventurerManager():

    @classmethod
    def getAnAdventurer(nameClassAdventurer: str):
        match nameClassAdventurer:
            case 'Mercenaire':
                return Mercenaire
            case 'Healer':
                return Healer
            case 'Tank':
                return Tank
            case _:
                raise Exception('no class match')

    

