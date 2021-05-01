allergy_dict = {
    0 : 'eggs',
    1 : 'peanuts',
    2 : 'shellfish',
    3 : 'strawberries',
    4 : 'tomatoes',
    5 : 'chocolate',
    6 : 'pollen',
    7 : 'cats'
}

class Allergies:

    def __init__(self, score):
        self._score = score

    def allergic_to(self, item):
        if item in self.lst:
            return True
        return False

    @property
    def lst(self):
        allergies = []
        iterator = 7
        score = self._score % 256
        while (iterator >= 0):
            if(score >= 2 ** iterator):
                allergies.append(allergy_dict[iterator])
                score -= 2 ** iterator
                iterator -= 1
            else:
                iterator -= 1
        return allergies