from random import randint

class Die():
    

    def __init__(self, sides=6):
        self.sides= sides
    

    def roll_die(self):
        print(str(randint(1, self.sides)))
        
dado6= Die()
dado10= Die(10)
dado20= Die(20)

for count in range(1, 11):
    dado6.roll_die()

print('\n')

for count in range(1, 11):
    dado10.roll_die()

print('\n')

for count in range(1, 11):
    dado20.roll_die()
        
