def is_isogram(string):
    string = string.replace(' ', '')
    string = string.replace('-', '')
    string = string.lower()
    # Alternative to strip spaces, hyphens and lowercase the string
    # string = string.translate(str.maketrans({ ' ' : None, '-' : None })).lower()

    # for i in l:
    #     if l.count(i) > 1:
    #         return False
    # return True

    # Alternative solution
    return len(list(string)) == len(set(string))
        


    
