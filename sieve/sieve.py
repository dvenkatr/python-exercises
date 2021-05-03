from itertools import filterfalse

def primes(limit):
    if limit <= 0:
        raise ValueError("Limit should be >=1")
    if limit == 1:
        return []

    prime_factors = range(2, limit + 1)
    i = 0
    while(prime_factors[i] != prime_factors[-1]):
        prime_factors = drop_multiples(prime_factors[i], prime_factors)
        i += 1
    return prime_factors

def drop_multiples(f, p):
    return list(filterfalse(lambda x: x % f == 0 and x != f, p))

    # for factor in primes:
    #     print(factor)
    #     primes = list(filterfalse(lambda x: x % factor == 0 and x != factor, primes))
    # return primes


print(primes(25))