# allergy_dict = {
#     0 : 'eggs',
#     1 : 'peanuts',
#     2 : 'shellfish',
#     3 : 'strawberries',
#     4 : 'tomatoes',
#     5 : 'chocolate',
#     6 : 'pollen',
#     7 : 'cats'
# }

# class Allergies:

#     def __init__(self, score):
#         self._score = score

#     def allergic_to(self, item):
#         if item in self.lst:
#             return True
#         return False

#     @property
#     def lst(self):
#         allergies = []
#         iterator = 7
#         score = self._score % 256
#         while (iterator >= 0):
#             if(score >= 2 ** iterator):
#                 allergies.append(allergy_dict[iterator])
#                 score -= 2 ** iterator
#                 iterator -= 1
#             else:
#                 iterator -= 1
#         return allergies

'''
# Alternative solution using bitwise operator &
'''

class Allergies:
    allergy_dict = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128,
    }

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return bool(self.score & self.allergy_dict[item])

    @property
    def lst(self):
        return [allergen for allergen, allergy_score in self.allergy_dict.items()
                if self.score & allergy_score]