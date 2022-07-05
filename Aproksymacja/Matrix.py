
def create_matrix(N, a1, a2, a3):
    a = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append(int(a1))
            elif i - 1 <= j <= i + 1:
                row.append(int(a2))
            elif i - 2 <= j <= i + 2:
                row.append(int(a3))
            else:
                row.append(int(0))
        a.append(row)
    return a


def vector_ones(len):
    vector = []
    for _ in range(len):
        vector.append(1.0)
    return vector


def vector_zeros(len):
    vector = []
    for _ in range(len):
        vector.append(0)
    return vector


def copy_vector(vector):
    copy = []
    for elem in vector:
        copy.append(elem)
    return copy


def vector_sub_vector(a, b):
    tmp = copy_vector(a)
    for i in range(len(tmp)):
        tmp[i] -= b[i]
    return tmp


def vector_multiply_number(a, b):
    vector = []
    for i in range(len(a)):
        vector.append(a[i] * b)
    return vector


def copy_matrix(matrix):
    copy = []
    for row in matrix:
        newRow = []
        for el in row:
            newRow.append(el)
        copy.append(newRow)
    return copy


def dot_product(a, b):
    copyA = copy_matrix(a)
    copyB = copy_vector(b)
    m = len(copyA)
    n = len(copyB)
    c = vector_zeros(m)

    for i in range(m):
        c[i] = 0
        for j in range(n):
            c[i] += copyA[i][j] * copyB[j]
    return c


def factorization_LU(a, b, size):
    U = a.copy()
    L = create_matrix(size, 1, 0, 0)
    P = create_matrix(size, 1, 0, 0)

    # matrix = L * U
    for k in range(size - 1):
        pivoting(U, L, P, k, size)
        for j in range(k + 1, size):
            L[j][k] = U[j][k] / U[k][k]
            U[j][k:size] = vector_sub_vector(U[j][k: size], vector_multiply_number(U[k][k:size], L[j][k]))

    # solve Ly = b
    b = dot_product(P, b)
    vectorY = vector_zeros(size)
    for i in range(size):
        sigma = 0
        for j in range(i):
            if j != i:
                sigma += L[i][j] * vectorY[j]
        vectorY[i] = (b[i] - sigma) / L[i][i]

    # solve Ux = y
    vectorX = vector_zeros(size)
    for i in range(size - 1, -1, -1):
        sigma = 0
        for j in range(i + 1, size):
            if j != i:
                sigma += U[i][j] * vectorX[j]
        vectorX[i] = (vectorY[i] - sigma) / U[i][i]
    return vectorX


def pivoting(U, L, P, i, size):
    pivot = abs(U[i][i])
    pivot_ind = i

    for j in range(i + 1, size):
        if abs(U[j][i]) > pivot:
            pivot = abs(U[j][i])
            pivot_ind = j

    if U[pivot_ind][i] == 0:
        return

    if pivot_ind != i:
        for j in range(size):
            if j >= i:
                U[i][j], U[pivot_ind][j] = U[pivot_ind][j], U[i][j]
            else:
                L[i][j], L[pivot_ind][j] = L[pivot_ind][j], L[i][j]
            P[i][j], P[pivot_ind][j] = P[pivot_ind][j], P[i][j]
