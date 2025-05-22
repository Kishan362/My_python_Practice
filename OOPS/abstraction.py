class megicman:
    # class object attribute
    flag = None
    def __init__(self, name ="newbie1", age = 0):
        
        self.name = name
        self.age = age
        if (age > 18):
            self.name = self.name
            self.age = self.age
            print('You can play this game')
            self.flag = True
            self.manavalue = None
            self.level = None
            self.attack = None
            self.speed = None
        else:
            self.name = None
            self.age = None
            print('Dear User, You are not old enough to play this game')
            self.flag = False
            self.manavalue = None
            self.level = None
            self.attack = None
            self.speed = None

    def mana(self, manavalue):
        if self.flag == False:
            self.manavalue = None
        else: 
            self.manavalue = manavalue
        return manavalue

    def megic_level(self, level):
        if self.flag == False:
            self.level = None
        else: 
            self.level = level
        return level
    def megic_attack(self, attack):
        if self.flag == False:
            self.attack = None
        else: 
            self.attack = attack
        return attack

    def run(self):
        print(f'{self.name} is running')

    def runningspeed(self, speed):
        if self.flag == False:
            self.speed = None
        else: 
            self.speed = speed
        return speed

    def all_details(self):
        if self.flag == False:
            print ('Error')        
        else: 
            print(f'Player Name : {self.name} Age: {self.age} attributes: {self.manavalue} mana, {self.level} level, {self.attack} attack, {self.speed} speed')

    @classmethod
    def add_things(cls, num1, num2):
        return cls('Meow' ,num1 + num2)

# Usage:
# megicman1 = megicman('aye', 19)


player1 = megicman.add_things(13, 13)
player1.mana(100)
player1.megic_level(100)
player1.megic_attack(100)
player1.all_details()