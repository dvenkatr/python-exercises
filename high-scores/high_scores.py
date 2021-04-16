def latest(scores: list) -> int:
    return scores.pop()


def personal_best(scores: list) -> int:
    return max(scores)

def personal_top_three(scores: list) -> list:
    top_three = []
    for i in range(3):
        if scores:
            x = max(scores)
            top_three.append(x)
            scores.remove(x)
    return top_three
    

