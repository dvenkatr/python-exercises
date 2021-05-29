brackets = {
    '[' : ']',
    '{' : '}',
    '(' : ')'
}

def is_paired(input_string : str) -> bool:

    unmatched_brackets = []
    
    for char in input_string:

        if char in brackets.keys():
            unmatched_brackets.append(char)
        elif char in brackets.values():
            if unmatched_brackets == []:
                return False
            elif char == brackets[unmatched_brackets[-1]]:
                unmatched_brackets.pop()
            else:
                return False

    if unmatched_brackets == []:
        return True
    else:
        return False

