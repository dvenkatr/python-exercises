def is_valid(isbn : str) -> bool:

    isbn = isbn.replace('-', '')

    if len(isbn) != 10 or not isbn[:-1].isdigit():
        return False

    if not isbn[-1].isdigit() and isbn[-1] != 'x' and isbn[-1] != 'X':
        return False

    if isbn[-1].isdigit():
        check = int(isbn[-1])
    else:
        check = 10

    for isbn_digit, multiplier in zip(isbn[:-1], range(10, 1, -1)):
        print(isbn_digit, multiplier)
        check += int(isbn_digit) * multiplier
    
    return check % 11 == 0

