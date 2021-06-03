def convert(input_grid):
    
    # Four rows per OCR character 
    # => total rows should be a multiple of 4
    if len(input_grid) % 4 != 0:
        raise ValueError("Invalid input: 4 rows per OCR expected")

    # The length of every row should be a multiple of 3
    # The last row of every OCR chunk (every 4th row) should be blank
    for row in range(0, len(input_grid)):
        if len(input_grid[row]) % 3 != 0:
            raise ValueError("Length of every row should be a multiple of 3")
        if (row + 1) % 4 == 0 and set(input_grid[row]) != {' '}:
            raise ValueError("Every fourth row should be blank")


    row_zero = {
    ' _ ' : {'0', '2', '3', '5', '6', '7', '8', '9'},
    '   ' : {'1', '4'}
    }

    row_one = {
        '| |' : {'0'},
        '  |' : {'1', '7'},
        ' _|' : {'2', '3'},
        '|_|' : {'4', '8', '9'},
        '|_ ' : {'5', '6'} 
    }

    row_two = {
        '|_|' : {'0', '6', '8'},
        '  |' : {'1', '4', '7'},
        '|_ ' : {'2'},
        ' _|' : {'3', '5', '9'},
    }

    numbers = ''

    for chunk in range(0, len(input_grid) - 3, 4):

        if chunk != 0:
            numbers = numbers + ','

        for col in range(0, len(input_grid[0]) - 2, 3):

            try:
                row_zero_options = row_zero[input_grid[chunk][col : col + 3]]
                row_one_options  = row_one[input_grid[chunk + 1][col : col + 3]]
                row_two_options  = row_two[input_grid[chunk + 2][col : col + 3]]
                number = row_zero_options & row_one_options & row_two_options
            except:
                number = {}

            if len(number) == 0:
                numbers += '?'
            else:
                numbers += list(number)[0]

    return numbers
