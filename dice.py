from random import randint

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(f"My roll was {randint(1,self.sides)} on a D{self.sides} die!")

my_dice = Dice(6)

for _ in range(10):
    my_dice.roll_die()
    
my_dice = Dice(10)

for _ in range(10):
    my_dice.roll_die()

my_dice = Dice(20)

for _ in range(10):
    my_dice.roll_die()