brackets = {
    '[' : ']',
    '{' : '}',
    '(' : ')'
}

def is_paired(input_string : str) -> bool:

    unmatched_brackets = ''
    
    for char in input_string:

        if char in brackets.keys() or char in brackets.values():
            if char in brackets.keys():
                unmatched_brackets += i
            else:
                try:
                    if char == brackets[unmatched_brackets[-1]]:
                        unmatched_brackets = unmatched_brackets[:-1]
                    else:
                        return False
                except:
                    return False

    if unmatched_brackets == '':
        return True
    else:
        return False


