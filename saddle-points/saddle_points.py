def saddle_points(matrix : list) -> list:

    num_of_rows = len(matrix)

    if num_of_rows == 0:
        return []
    
    if any(len(matrix[r]) != len(matrix[r + 1]) for r in range(0, num_of_rows - 1)):
        raise ValueError("Error: irregular matrix")

    # Create column matrix similar to row matrix
    # col_matrix = []
    # num_of_col = len(matrix[0])
    # for c in range(0, num_of_col):
    #     col = []
    #     for row in matrix:
    #         col.append(row[c])
    #     col_matrix.append(col)

    # Create column matrix similar to row matrix
    col_matrix = list(zip(*matrix))

    num_of_col = len(matrix[0])

    saddles = []
    for r in range(0, num_of_rows):
        for c in range(0, num_of_col):
            if matrix[r][c] == max(matrix[r]) and matrix[r][c] == min(col_matrix[c]):
                saddles.append({
                    'row' : r + 1,
                    'column' : c + 1
                })
    return saddles




