SUBLIST = 'Sub'
SUPERLIST = 'Super'
EQUAL = 'Equal'
UNEQUAL = 'Unequal'

def sublist(list_one : list, list_two : list) -> str:
    
    if list_one == list_two:
        return EQUAL

    if len(list_one) == len(list_two):
        return UNEQUAL

    if len(list_one) > len(list_two):
        big_list = list_one
        small_list = list_two
        default = SUPERLIST
    else:
        big_list = list_two
        small_list = list_one
        default = SUBLIST

    for i in range(0, len(big_list) - len(small_list) + 1):
        if big_list[i : i + len(small_list)] == small_list:
            return default
    return UNEQUAL

