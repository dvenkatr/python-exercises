'''
# Solution without using sets


def equilateral(sides : list) -> bool:
    if not is_triangle(sides):
        return False
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    return False
    

def isosceles(sides : list) -> bool:
    if not is_triangle(sides):
        return False
    for i in range(0, 3):
        if sides[i % 3] == sides[(i+1) % 3]:
            return True
    return False


def scalene(sides : list) -> bool:
    if not is_triangle(sides):
        return False
    if sides[0] != sides[1] and sides[1] != sides[2]:
        return True
    return False


def is_triangle(sides : list) -> list:
    if any(side <= 0 for side in sides):
        return False
    if len(sides) != 3:
        return False
    for i in range(0, 3):
        if sides[i % 3] + sides[(i + 1) % 3] < sides[(i + 2) % 3]:
            return False
    return True

'''

'''
# Alternative solution using sets
# Inequality test: a + b > c or sum(a, b, c) > 2c even if c = max(a, b, c)


def equilateral(sides : list) -> bool:
    if not is_triangle(sides):
        return False
    if num_of_equal_sides(sides) == 1:
        return True
    return False
    

def isosceles(sides : list) -> bool:
    if not is_triangle(sides):
        return False
    if num_of_equal_sides(sides) < 3:
        return True
    return False


def scalene(sides : list) -> bool:
    if not is_triangle(sides):
        return False
    if num_of_equal_sides(sides) == 3:
        return True
    return False


def is_triangle(sides : list) -> list:
    if not all(sides) or len(sides) != 3 or 2*max(sides) >= sum(sides):
        return False
    return True


def num_of_equal_sides(sides : list) -> int:
    return len(set(sides))
'''

'''
Alternative using decorators
'''

def is_valid(function):
    return lambda sides: all(sides) and 2 * max(sides) < sum(sides) and function(sides)

@is_valid
def is_equilateral(sides):
    return len(set(sides)) == 1

@is_valid
def is_isosceles(sides):
    return len(set(sides)) < 3

@is_valid
def is_scalene(sides):
    return len(set(sides)) == 3