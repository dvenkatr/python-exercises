'''
# Solution without recursion


def steps(number : int) -> int:
    if number <= 0:
        raise ValueError("Number should be a positive non-zero integer")

    count = 0
    while(number != 1):
        count += 1
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1

    return count

'''

'''
# Solution using recursion
'''

def steps(number : int, count : int = 0) -> int:
    if number <= 0:
        raise ValueError("Number should be a positive non-zero integer")

    if int(number) == 1:
        return count

    if number % 2 == 0:
        return steps(number/2, count + 1)
    else:
        return steps (number * 3 + 1, count + 1)

