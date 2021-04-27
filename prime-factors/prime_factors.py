def factors(value):
    
    if value <= 0:
        raise ValueError("Number should be a non-zero positive integer")

    prime_factors = []
    divisor = 2

    while value != 1:
        if value % divisor == 0:
            prime_factors.append(divisor)
            value /= divisor
            print(value, divisor, prime_factors)
        else:
            divisor += 1
    return prime_factors


'''
This solution uses recursion
For large values, the maximum recursion depth will be exceeded
The recursion limit can be increased using sys.setrecursionlimit()

Also note
1. The right side of the default assignment for an argument is only evaluated once, when the function is defined
2. So when factors() is called w/o prime_factors, prime_factors = value from 1.
3. prime_factors -> 0x100 = None
4. In line 11, if prime_factors -> 0x100 = None, prime_factors -> 0x200 = [] 
5. The factors are added to 0x200


import sys
sys.setrecursionlimit(10000)

def factors(value, divisor = 2, prime_factors = None):
    
    if value <= 0:
        raise ValueError("Number should be a non-zero positive integer")

    if prime_factors == None: # See explanation above
        prime_factors = []

    if value == 1:
        return prime_factors

    if value % divisor == 0:
        prime_factors.append(divisor)
        return factors(value/divisor, divisor, prime_factors)
    else:
        divisor += 1
        return factors(value, divisor, prime_factors)

'''
