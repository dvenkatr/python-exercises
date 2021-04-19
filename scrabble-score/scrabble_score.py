def score(word):

    letter_score = {
        'D' : 2, 'G' : 2,
        'B' : 3, 'C' : 3, 'M' : 3, 'P' : 3,
        'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4, 'Y' : 4,
        'K' : 5,
        'J' : 8, 'X' : 8,
        'Q' : 10, 'Z' : 10
    }

    return sum(1 if i not in letter_score else letter_score[i] for i in word.upper())


''' 
Solution with extensions to include double, triple letters and words
'''

def score_extended(word:str, double_or_triple_letter=None, double_word=False, triple_word=False) -> int:

    if double_or_triple_letter == None:
        double_or_triple_letter = [1 for i in range(0, len(word))]
    
    if len(word) != len(double_or_triple_letter):
            raise ValueError("Cannot compute score: double_or_triple_letter list should be of the same length as the word")

    for i in double_or_triple_letter:
        if i != 1 and i != 2 and i !=3:
            raise ValueError("A letter's score may be unchanged, double or triple only")

    if double_word is True:
        double_word = 2
    else:
        double_word = 1

    if triple_word is True:
        triple_word = 3
    else:
        triple_word = 1

    word = word.upper()

    letter_score = {
        'D' : 2, 'G' : 2,
        'B' : 3, 'C' : 3, 'M' : 3, 'P' : 3,
        'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4, 'Y' : 4,
        'K' : 5,
        'J' : 8, 'X' : 8,
        'Q' : 10, 'Z' : 10
    }
    
    print("Letters in the word ", list(word))
    print("Double or triple letter list ", double_or_triple_letter)
    print("Double word multiplier", double_word)
    print("Triple word multiplier", triple_word)
    print("Score ", sum(1 * double_or_triple_letter[i] if word[i] not in letter_score else letter_score[word[i]] * double_or_triple_letter[i] for i in range(0, len(word))) * double_word * triple_word)

    return sum(1 * double_or_triple_letter[i] if word[i] not in letter_score else letter_score[word[i]] * double_or_triple_letter[i] for i in range(0, len(word))) * double_word * triple_word

score_extended("zoox")
score_extended("zoox", None, True, False)
score_extended("zoox", [1, 3, 1, 2], True, False)