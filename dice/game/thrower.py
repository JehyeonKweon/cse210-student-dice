import random

# TODO: Define the Thrower class here.
class Thrower:

    def __init__(self):
        self.dice = [0, 0, 0, 0, 0]
        self.throw = True

    def can_throw(self):
        for die in self.dice:
            if die == 1 or die ==5:
                return self.throw == True
            else:
                pass
        return self.throw == False

    def throw_dice(self):
        for die in range(0,5):
            self.dice[die] = random.randint(1,6)
        return self.dice
            
    def get_points(self):
        point = 0
        for die in self.dice:
            if die == 1:
                point += 100
            elif die == 5:
                point += 50
            else:
                point += 0
        return point