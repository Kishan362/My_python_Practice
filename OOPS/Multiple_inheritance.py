class User() :

    def sign_in(self) :
        print('logged in')

class Wizard(User) :
    def __init__(self, name, power) :
        self.name = name
        self.power = power

    def attack(self) :
        print(f'attacking with power of {self.power}')

class Archer(User) :
    
    def __init__(self, name, num_arrows) :
        self.name = name
        self.num_arrows = num_arrows
    
    def checkarrows(self) :
        print(f'{self.num_arrows} remaining')

    def attack(self) :
        print(f'attacking with arrows : arrows left - {self.num_arrows}')

class Hybrid(Wizard, Archer) :
    def __init__(self, name, power, arrows) :
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = Hybrid('XXX-Borg', 50, 100)
hb1.checkarrows()
hb1.attack()
print(hb1.name)



# wizard1 = Wizard('Merlin', 50)
# archer1 = Archer('Robin', 100)

# wizard1.sign_in()
# archer1.sign_in()

# wizard1.attack()
# archer1.attack()

# print(isinstance(wizard1, User))