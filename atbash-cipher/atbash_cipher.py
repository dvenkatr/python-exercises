from string import punctuation

punctuation_incl_space = punctuation + ' '

def strip_punctuation(text):
    return text.translate(str.maketrans('', '', punctuation_incl_space))

def code(c):
    if c.isdigit():
        return c
    if c.isalpha():
        return chr(122 - ord(c) + 97)

def encode(plain_text):
    plain_text = strip_punctuation(plain_text).lower()
    encoded_text = ''
    for char in plain_text: 
        encoded_text += code(char)
    return ' '.join(encoded_text[i : i + 5] for i in range(0, len(encoded_text), 5))

def decode(ciphered_text):
    ciphered_text = strip_punctuation(ciphered_text).lower()
    decoded_text = ''
    for char in ciphered_text:
        decoded_text += code(char)
    return decoded_text