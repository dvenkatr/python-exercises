def annotate(minefield : list) -> list:

    validate(minefield)

    # Loop through the minefield. Convert row string to list. Replace ' ' with "score"

    for row in range(0, len(minefield)):
        minefield[row] = list(minefield[row])
        for col in range(0, len(minefield[row])):
            if minefield[row][col] == ' ':

                score = find_score(row, col, minefield)
                if score != 0:
                    minefield[row][col] = str(score)

        minefield[row] = "".join(minefield[row])

    return minefield


def find_score(row, col, minefield):

    score = 0
    
    row_lower = max(0, row - 1)
    row_upper = min(len(minefield) - 1, row + 1) + 1

    col_lower = max(0, col - 1)
    col_upper = min(len(minefield[0]) - 1, col + 1) + 1

    # Loop through adjancent cells excluding the current cell to check for mines

    for r in range(row_lower, row_upper):
        for c in range(col_lower, col_upper):
            if r == row and c == col:
                continue
            else:
                if minefield[r][c] == '*':
                    score += 1

    return score

def validate(minefield):

    # Validate that all rows are of equal length
    # and that all cells are ' ' or '*'
    for row in range(0, len(minefield)):
        if row != len(minefield) - 1:
            if len(minefield[row]) != len(minefield[row + 1]):
                raise ValueError("Invalid input: rows must be of equal length")
        
        for col in range(0, len(minefield[0])):
            if minefield[row][col] != '*' and minefield[row][col] != ' ':
                raise ValueError("Invalid input: only '*' or ' ' allowed")