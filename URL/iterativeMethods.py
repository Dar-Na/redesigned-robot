import time

from vector_methods import *
from matrix_methods import *


def jacobi(a, b):
    time0 = time.time()
    iterations = 0
    matrixA = copy_matrix(a)
    vectorB = copy_vector(b)
    tmpX = vector_zeros(len(matrixA))
    x = copy_vector(tmpX)

    while True:
        for i in range(len(matrixA)):
            sigma = 0
            for j in range(len(matrixA)):
                if i != j:
                    sigma += matrixA[i][j] * x[j]
            tmpX[i] = (vectorB[i] - sigma) / matrixA[i][i]
        x = copy_vector(tmpX)
        res = vector_sub_vector(dot_product(matrixA, x), vectorB)

        # if norm(res) < pow(10, -9):
        #     break
        # iterations += 1

        try:
            if norm(res) < pow(10, -9):
                break
            iterations += 1
        except OverflowError:
            print("OverflowError in iteration ", iterations)
            break

    print("Jacobi method")
    print('time:', time.time() - time0)
    print('iterations:', iterations)
    print()
    return time.time() - time0


def gaussaSeilda(a, b):
    time0 = time.time()
    iterations = 0
    matrixA = copy_matrix(a)
    vectorB = copy_vector(b)
    vectorX = vector_zeros(len(matrixA[0]))

    while True:
        for i in range(len(matrixA)):
            sigma = 0
            for j in range(len(matrixA)):
                if i != j:
                    sigma += matrixA[i][j] * vectorX[j]
            vectorX[i] = (vectorB[i] - sigma) / matrixA[i][i]
        res = vector_sub_vector(dot_product(matrixA, vectorX), vectorB)

        # if norm(res) < pow(10, -9):
        #     break
        # iterations += 1

        try:
            if norm(res) < pow(10, -9):
                break
            iterations += 1
        except OverflowError:
            print("OverflowError in iteration ", iterations)
            break

    print("Gauss-Seild method")
    print('time:', time.time() - time0)
    print('iterations:', iterations)
    print()
    return time.time() - time0


def factorization_LU(a, b):
    time0 = time.time()
    m = len(a)
    matrixA = copy_matrix(a)
    vectorB = copy_vector(b)

    L = matrix_identity(m, m)
    U = copy_matrix(a)
    for k in range(m - 1):
        for j in range(k + 1, m):
            L[j][k] = U[j][k] / U[k][k]
            U[j][k:m] = vector_sub_vector(U[j][k: m], vector_multiply_number(U[k][k:m], L[j][k]))

    # solve Ly = b
    vectorY = vector_zeros(m)
    for i in range(m):
        sigma = 0
        for j in range(i):
            if j != i:
                sigma += L[i][j] * vectorY[j]
        vectorY[i] = (b[i] - sigma) / L[i][i]

    # solve Ux = y
    vectorX = vector_zeros(m)
    for i in range(m - 1, -1, -1):
        sigma = 0
        for j in range(i + 1, m):
            if j != i:
                sigma += U[i][j] * vectorX[j]
        vectorX[i] = (vectorY[i] - sigma) / U[i][i]

    res = vector_sub_vector(dot_product(matrixA, vectorX), vectorB)
    # results
    print("LU method")
    print('time:', time.time() - time0)
    print("Residuum norm:", norm(res))
    print()
    return time.time() - time0


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
