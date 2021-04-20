from string import punctuation

def abbreviate(words : str) -> str:

    # Treat hyphen as a word delimiter i.e. replace it with space
    words = words.replace('-', ' ')
    # Remove all other punctuation
    words = words.translate(str.maketrans('', '', punctuation))

    '''
    # Longer but (slightly) more efficient solution
    
    index = 0
    acronym = words[index]
    index = words.find(' ', index) + 1
    while(index != 0):
        if words[index] == ' ':
            index += 1
        else:
            acronym += words[index]
            index = words.find(' ', index) + 1
    return acronym.upper()
    '''

    '''
    # Alternative solution that is more succinct but less efficient
    '''

    return "".join([word[0] for word in words.split() if word != ' ']).upper()

