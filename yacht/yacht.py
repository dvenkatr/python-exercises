"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.

ONES = lambda dice: sum(x for x in dice if x == 1)
TWOS = lambda dice: sum(x for x in dice if x == 2)
THREES = lambda dice: sum(x for x in dice if x == 3)
FOURS = lambda dice: sum(x for x in dice if x == 4)
FIVES = lambda dice: sum(x for x in dice if x == 5)
SIXES = lambda dice: sum(x for x in dice if x == 6)

def FULL_HOUSE (dice):
    sum = 0
    count_list = []
    for x in dice:
        count_list.append(dice.count(x))
        sum += x
    if (3 in count_list) and (2 in count_list):
        return sum
    else:
        return 0

# def FOUR_OF_A_KIND (dice):
#     num = 0
#     count_list = []
#     for x in dice:
#         if dice.count(x) == 4:
#             return x * 4
#     return 0

FOUR_OF_A_KIND = lambda dice: sum(x*4 for x in set(dice) if dice.count(x) >= 4)

def LITTLE_STRAIGHT (dice):
    for x in (1,5):
        if dice.count(x) != 1:
            return 0
    return 30

def BIG_STRAIGHT (dice):
    for x in (2,6):
        if x not in dice:
            return 0
    return 30

CHOICE = lambda dice: sum(dice)

# def YACHT (dice): 
#     print("Calling YACHT")
#     for x in dice:
#         print(x)
#         if x != 5: 
#             print ("x not 5")
#             return 0
#     print("For loop ended")
#     return 50

YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0

def score(dice, category):
    if any(not 0 < x < 7 for x in dice):
        raise ValueError("Invalid dice {}".format(dice))
    return category(dice)

a = score([0, 1, 2, 3, 4], YACHT)
print(a)