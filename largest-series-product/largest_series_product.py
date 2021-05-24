from functools import reduce

def product(a):
    a = map(lambda x : int(x), a)
    return reduce(lambda x, y : x * y, a, 1)

def largest_product(series, size):

    if series == '' and size !=0:
        raise ValueError("Series is empty")

    if size < 0:
        raise ValueError("Size must be positive")

    if size > len(series):
        raise ValueError("Size must <= series")

    max_product = 0
    for i in range(0, len(series) - size + 1):
        subset = list(series[i : i + size])
        max_product = max(product(subset), max_product)
    return max_product