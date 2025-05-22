class Game_character :
    def __init__(self, name, health, power):
        self.name = str(name)
        self.health = int(health)
        self.power = int(power)
    def attack(self):
        print(f'{self.name} is attacking with {self.power} power')
    def introduction(self):
        print(f'Player Name : {self.name} Health: {self.health} Power: {self.power}')




player1 = Game_character('Axel', 100, 50)
player1.introduction()
