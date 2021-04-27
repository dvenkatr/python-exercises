def square(number : int) -> int:
    if number <= 0 or number > 64:
        raise ValueError("Number has to be a number between 1 and 64")
    return 2 ** (number - 1)


def total() -> int:
    # Sum of geometric series = a * (1-r^n) / (1-r)
    # a = 1, r = 2, n = 64
    return 2 ** 64 - 1
    
