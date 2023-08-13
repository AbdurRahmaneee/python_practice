class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        # User.attack(self)
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows {self.num_arrows}')

wizard1 = Wizard('merlin', 60, 'merling@gmail.com')
archer1 = Archer('robin', 30)
# print(wizard1.email)
print(dir(wizard1))
# def player_attack(char):
#     char.attack()

# for char in (wizard1, archer1):
#     char.attack()