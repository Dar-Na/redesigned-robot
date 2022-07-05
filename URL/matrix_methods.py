def copy_matrix(matrix):
    copy = []
    for row in matrix:
        newRow = []
        for el in row:
            newRow.append(el)
        copy.append(newRow)
    return copy


def matrix_sub_matrix(a, b):
    tmp = copy_matrix(a)
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            tmp[i][j] -= b[i][j]
    return tmp


def matrix_add_matrix(a, b):
    tmp = copy_matrix(a)
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            tmp[i][j] += b[i][j]
    return tmp


def matrix_zeros(x, y):
    matrix = []
    for _ in range(y):
        row = []
        for _ in range(x):
            row.append(int(0))
        matrix.append(row)
    return matrix

def matrix_identity(x, y):
    matrix = []
    for i in range(y):
        row = []
        for j in range(x):
            if i == j:
                row.append(int(1))
            else:
                row.append(int(0))
        matrix.append(row)
    return matrix

