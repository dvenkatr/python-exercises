one_dict = {
    '0' : '',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
}

teen_dict = {
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eightteen',
    '19' : 'nineteen',
}

ten_dict = {
    '2' : 'twenty',
    '3' : 'thirty',
    '4' : 'forty',
    '5' : 'fifty',
    '6' : 'sixty',
    '7' : 'seventy',
    '8' : 'eighty',
    '9' : 'ninety',
}

word_dict = {
    12 : 'trillion ',
    9 : 'billion ',
    6 : 'million ',
    3 : 'thousand ',
    2 : 'hundred ',
}

def say(number):

    numstr = str(number)
    index = len(numstr)
    spell = ''

    if number < 0:
        raise ValueError("Error: negative number")

    if number == 0:
        return 'zero'

    # Handle numbers > 999 trillion by splitting it into head + trillion
    if index >= 16:
        spell += say(int(numstr[:(index - 12)])) + ' ' + word_dict[12] + say(int(numstr[-12:]))
        return spell
        
    while index >= 4:
        if index % 3 != 0:
            n = index % 3
        else:
            n = 3
            
        head = numstr[:n]
        rest = numstr[n:]

        if find_prefix(head) != '':
            spell += find_prefix(head) + ' ' + word_dict[len(rest)]

        numstr = rest
        index -= n

    # Handle numbers < 999
    if index <= 3:
        spell += find_prefix(numstr)

    return spell.strip()

def find_prefix(smallstr):
    count = len(smallstr)
    if count > 4:
        return say(smallstr)
    if count == 3:
        return triple_digit_prefix(smallstr)
    if count == 2:
        return double_digit_prefix(smallstr)
    if count == 1:
        return single_digit_prefix(smallstr)

def single_digit_prefix(s):
    return one_dict[s]

def double_digit_prefix(s):
    # 08
    if s[0] == '0':
        return single_digit_prefix(s[1:])
    # 18
    if s[0] == '1':
        return teen_dict[s]
     # 20
    if s[1] == '0':
        return ten_dict[s[0]]
     # 28
    else:
        return ten_dict[s[0]] + '-' + single_digit_prefix(s[1:])

def triple_digit_prefix(s):
     # 017
    if s[0] == '0':
        return double_digit_prefix(s[1:])
    # 567
    else:
        return one_dict[s[0]] + ' ' + word_dict[2] + double_digit_prefix(s[1:])
        

# print('----------')
# print(say(0))
# print(say(1))
# print(say(9))
# print('----------')
# print(say(10))
# print(say(19))
# print('----------')
# print(say(60))
# print(say(99))
# print('----------')
# print(say(100))
# print(say(105))
# print(say(110))
# print(say(199))
# print(say(200))
# print(say(201))
# print(say(211))
# print(say(220))
# print(say(999))
# print('----------')
# print(say(1000))
# print(say(1123))
# print(say(9568)) # nine thousand..
# print('----------')
# print(say(19568)) # nineteen thousand..
# print(say(39568)) # thirty nine thousand..
# print(say(100000))
# print(say(439568)) # four hundred and thirty nine thousand..
# print('----------')
# print(say(1000000)) # one million
# print(say(9876543)) # nine million..
# print(say(10000000)) # ten million
# print(say(98765432)) # ninety eight million..
# print(say(100000000)) # one hundred million
# print(say(987654321)) # 987 million..
# print('----------')
# print(say(1000000000)) # one billion
# print(say(9876543210)) # nine billion..
# print('----------')
# print(say(1234567879876543210) 
# == "one million two hundred thirty-four thousand five hundred sixty-seven trillion 
#      eight hundred seventy-nine billion eight hundred seventy-six million five hundred forty-three thousand two hundred ten")
