# Generating Random Values
import random

# for i in range(3):
#     print(random.randint(10,20))

# members = ['John', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(members)
# print(leader)

#exercise
# Class caled Dice
# method called roll()

class Dice:
    def roll(self):
        first = random.randit(1, 6)
        second = random.randit(1, 6)
        return first, second

dice = Dice()
print(dice.roll())
