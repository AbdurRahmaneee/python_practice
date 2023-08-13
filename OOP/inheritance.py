class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows {self.num_arrows}')

wizard1 = Wizard('merlin', 60)
archer1 = Archer('robin', 30)
print(wizard1.attack())

def player_attack(char):
    char.attack()

# for char in (wizard1, archer1):
#     char.attack()