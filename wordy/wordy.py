from functools import reduce

import numbers

import re

# Define accepted functions
def plus(arg1, arg2):
    return arg1 + arg2

def minus(arg1, arg2):
    return arg1 - arg2

def into(arg1, arg2):
    return arg1 * arg2

def by(arg1, arg2):
    return arg1 / arg2

def expo(arg1, arg2):
    return arg1 ** arg2

# Accepted operators
operator_dict = {
    'plus'  : plus,
    'minus' : minus,
    'into'  : into,
    'by'    : by,
    'expo'  : expo
}

def answer(question):

    def apply(result, expr):
        arg1 = result
        arg2, func = expr
        return func(arg1, arg2)

    # Validate question and get the numbers and operators
    arguments, operators = parse(question)

    return reduce(apply, zip(arguments, operators), 0)

# Validate and parse the input to return arguments (numbers) and operators
def parse(question):

    if not question.startswith("What is "):
        raise ValueError("Invalid question")

    if not question.endswith("?"):
        raise ValueError("Input is not a question")

    parsed = question.replace("What is ", "") \
                        .replace("multiplied by", "into") \
                        .replace("divided by", "by") \
                        .replace("?", "")

    parsed = re.sub("raised to the ([0-9]+)th power", "expo \\1", parsed)
    
    if parsed == "":
        raise ValueError("Please check your input: no numbers were provided")

    parsed = parsed.split()

    if len(parsed) % 2 != 1:
        raise ValueError("Please check your input: unexpected numbers or operators")

    arguments = list(map(int, parsed[0 :: 2]))
    operators = list(map(lambda x : operator_dict.get(x), ['plus'] + parsed[1 :: 2]))

    if not all(map(lambda i : isinstance(i, numbers.Number), arguments)):
        raise ValueError("Please check your input: alternate numbers and operators expected")

    if any(map(lambda x : x == None, operators)):
        raise ValueError("Please check your input: alternate numbers and operators expected")

    return arguments, operators