def is_armstrong_number(number):
    digits = len(str(number))
    result = 0
    for i in str(number):
        i = int(i)
        result = result + i**digits
    return (result == number)
