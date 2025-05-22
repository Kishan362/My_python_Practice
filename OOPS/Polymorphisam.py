# polimorphism 
# poly means many and morphisam is 
# class
class User() :
    def __init__(self, name) :
        self._name = name

    def sign_in(self) :
        print(f'{self._name} has logged in')

class Wizard(User) :
    def __init__(self, name, power) :
        super().__init__(name)
        self.power = power

    def attack(self) :
        print(f'attacking with power of {self.power}')

class Archer(User) :
    
    def __init__(self, name, num_arrows) :
        super().__init__(name)
        self.num_arrows = num_arrows

    def attack(self) :
        print(f'attacking with arrows : arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

wizard1.sign_in()
archer1.sign_in()

wizard1.attack()
archer1.attack()

print(isinstance(wizard1, User))

#polymosphisam

for char in [wizard1, archer1] :
    char.attack()

def player_attack(char) :
    char.attack()

player_attack(wizard1)
player_attack(archer1)

