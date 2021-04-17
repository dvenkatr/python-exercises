class Matrix:
    def __init__(self, matrix_string):

        self.matrix = []
        for row_string in matrix_string.split('\n'):
            row = list(map(int, row_string.split()))
            self.matrix.append(row)
            # self.matrix.append([int(col) for col in row.split()])
            # self.matrix.append(list(map(int, row.split())))

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]

x = Matrix("89 1903 3\n18 3 1\n9 4 800")