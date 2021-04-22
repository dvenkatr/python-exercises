''' 
# Solution that does not mutate the list
'''

def latest(scores: list) -> int:
    return scores[-1]

def personal_best(scores: list) -> int:
    return max(scores)

def personal_top_three(scores: list) -> list:
    return sorted(scores, reverse=True)[0:3]

        


    

