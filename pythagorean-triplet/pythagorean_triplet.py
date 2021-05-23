import math

def triplets_with_sum(number):
    return [[i, j, number - i - j] 
    for i in range(1, number - 5) 
    for j in range(i + 1, math.floor((number - i) / 2) + 1) 
    if number - i - j > j and i ** 2 + j ** 2 == (number - i - j) ** 2]

    