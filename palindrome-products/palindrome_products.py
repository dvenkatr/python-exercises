'''
# More efficient solution 
# Tests run in 17.7s vs. 22.4s
'''

from itertools import combinations_with_replacement
import functools


def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor should be smaller than max_factor")
    palindromes = find_product_palindromes(min_factor, max_factor)
    return functools.reduce(max_fn, palindromes, (None, []))

    
def max_fn(current_max, element):
    if current_max[0] is None:
        return (element[0], [element[1]])
    if current_max[0] > element[0]:
        return current_max
    if current_max[0] < element[0]:
        return (element[0], [element[1]])
    else:
        current_max[1].append(element[1])
        return current_max


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor should be smaller than max_factor")
    palindromes = find_product_palindromes(min_factor, max_factor)
    return functools.reduce(min_fn, palindromes, (None, []))

    
def min_fn(current_min, element):
    if current_min[0] is None:
        return (element[0], [element[1]])
    if current_min[0] < element[0]:
        return current_min
    if current_min[0] > element[0]:
        return (element[0], [element[1]])
    else:
        current_min[1].append(element[1])
        return current_min


def find_product_palindromes(min_factor, max_factor):
    for x, y in combinations_with_replacement(range(min_factor, max_factor + 1), 2):
        p = x * y  
        if str(p) == str(p)[::-1]:
            yield p, [x, y]


'''
# Less efficient solution
# Factors are recomputed after the palindromes are identified
# Tests run in 22.4s vs. 17.1s


from itertools import combinations_with_replacement
import math


def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor should be smaller than max_factor")
    product_palindromes = find_product_palindromes(min_factor, max_factor)
    try:
        max_product_palindrome = max(product_palindromes)
        return max_product_palindrome, factors(max_product_palindrome, min_factor, max_factor)
    except ValueError:
        return (None, [])
    

def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min_factor should be smaller than max_factor")
    product_palindromes = find_product_palindromes(min_factor, max_factor)
    try:
        min_product_palindrome = min(product_palindromes)
        return min_product_palindrome, factors(min_product_palindrome, min_factor, max_factor)
    except ValueError:
        return (None, [])


def factors(num, min_factor, max_factor):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0 and i in range(min_factor, max_factor + 1) and num/i in range(min_factor, max_factor + 1):
            factors.append([i, int(num/i)])
    return factors


def find_product_palindromes(min_factor, max_factor):
    factors_iterator = combinations_with_replacement(range(min_factor, max_factor + 1), 2)
    products_iterator = map(multiply, factors_iterator)
    return filter(is_palindrome, products_iterator)


def multiply(nums_as_tuple):
    return nums_as_tuple[0] * nums_as_tuple[1]


def is_palindrome(num):
    return str(num) == str(num)[::-1]
    
'''