def square_of_sum(n):
    return (n * (n+1))**2 / 4


def sum_of_squares(n):
    return (n * (n+1) * (2*n+1)) / 6


def difference_of_squares(n):
    return abs(sum_of_squares(n) - square_of_sum(n))
