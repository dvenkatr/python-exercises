import random

ATTRIBUTES = (
    'strength',
    'dexterity',
    'constitution',
    'intelligence',
    'wisdom',
    'charisma'
)

def modifier(constitution):
    return ((constitution - 10) // 2)

class Character:
    def __init__(self):
        for a in ATTRIBUTES:
            setattr(self, a, self.get_score())
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return self.get_score()
        
    def get_score(self):
        dice = []
        for i in range(4):
            dice.append(random.randint(1, 6))
        dice.remove(min(dice))
        return sum(dice)