import math

def classify(number: int) -> str:

    if(number <= 0):
        raise ValueError("Number must be a positive integer >0")

    if factorise(number) == 1 or factorise(number) < number:
        return 'deficient'
    if factorise(number) > number:
        return 'abundant'
    else:
        return 'perfect'

def factorise(number: int) -> int:
    factors = [1]
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0 and i != number // i:
            factors.append(i + number // i)
        if number % i == 0 and i == number // i:
            factors.append(i)
    return sum(factors)

