def sum_of_multiples(limit, multiples):
    return sum(set(i * j for i in range(1, limit) for j in multiples if i * j < limit))

