
def score(x, y):
    distance = ((y-0)**2 + (x-0)**2)**0.5
    score = 0

    if distance <= 1:
        score = 10
    elif distance > 1 and distance <= 5:
        score = 5
    elif distance  > 5 and distance <= 10:
        score = 1

    return score

print(score(0.8, 0.5))