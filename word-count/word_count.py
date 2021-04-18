from string import punctuation

def count_words(sentence):

    # Replace delimiters with space, and convert string to lower case
    sentence = sentence.translate(str.maketrans({ 
        '!' : ' ',
        '?' : ' ',
        '.' : ' ',
        ';' : ' ',
        ',' : ' ',
        ':' : ' ',
        '_' : ' ',
        '\n' : ' ', 
        '\t' : ' '})).lower()

    # Remove all punctuation except apostrophe    
    punctuation_except_apostrophe = punctuation.replace("'", "")
    sentence = sentence.translate(str.maketrans(',', ' ', punctuation_except_apostrophe))

    # Get words from sentence
    l = sentence.split()

    # Strip quotes around words
    def handle_quotes(i):
        stripped = i.strip("'")
        return stripped

    l = list(map(handle_quotes, l))

    # Get unique words from sentence
    s = set(l)

    # Count words
    word_count = {}
    for i in s:
        word_count[i] = l.count(i)
    return word_count