#private variables
#doing _ befor variable name makes it private 

class Game_character :
    def __init__(self, name, health, power):
        self._name = str(name)
        self._health = int(health)
        self._power = int(power)
    def attack(self):
        print(f'{self._name} is attacking with {self._power} power')
    def introduction(self):
        print(f'Player Name : {self._name} Health: {self._health} Power: {self._power}')




player1 = Game_character('Axel', 100, 50)
player1.introduction()