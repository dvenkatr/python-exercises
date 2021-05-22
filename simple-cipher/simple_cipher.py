from itertools import cycle
import math
from random import randint

class Cipher:
    def __init__(self, key=""):
        if key == "":
            for i in range(20):
                key += chr(randint(97,122))
        self.key = key


    def encode(self, text):

        def encode_char(x):
            code = ord(x[0]) + ord(x[1]) - 97
            if code > 122:
                code -= 26
            return chr(code)

        return "".join(map(encode_char, zip(text, cycle(self.key))))


    def decode(self, text):

        def decode_char(x):
            decode = ord(x[0]) - (ord(x[1]) - 97)
            if decode < 97:
                decode += 26
            return chr(decode)

        return "".join(map(decode_char, zip(text, cycle(self.key))))


