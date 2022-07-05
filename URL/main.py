from matplotlib import pyplot as plt

from iterativeMethods import *
from Matirx import *


if __name__ == "__main__":
    # A
    matrix = Matrix(187726)

    matrix.N = 10
    print(matrix.create_matrix_a())

    matrixA = matrix.create_matrix_a()
    vectorB = matrix.create_vector_b()
    # B
    timeJacobi = jacobi(matrixA, vectorB)
    timeGauss = gaussaSeilda(matrixA, vectorB)

    print("timeJacobi - timeGauss = ", timeJacobi - timeGauss)
    print()

    # C
    matrixC = matrix.create_matrix_c()
    vectorB = matrix.create_vector_b()

    # timeJacobi = jacobi(matrixC, vectorB)
    # timeGauss = gaussaSeilda(matrixC, vectorB)

    # D
    factorization_LU(matrixC, vectorB)

    # E
    N = [100, 500, 1000, 2000, 3000]
    timeJacobi = []
    timeGauss = []
    timeLU = []
    for n in N:
        print("Size: ", n)
        matrix.N = n
        matrixA = matrix.create_matrix_a()
        vectorB = matrix.create_vector_b()

        timeJacobi.append(jacobi(matrixA, vectorB))
        timeGauss.append(gaussaSeilda(matrixA, vectorB))
        timeLU.append(factorization_LU(matrixA, vectorB))

    plt.plot(N, timeJacobi, label="Jacobi", color="green")
    plt.plot(N, timeGauss, label="Gauss-Seild", color="black")
    plt.plot(N, timeLU, label="LU", color="red")
    plt.legend()
    plt.xlabel("Rozmiar N")
    plt.ylabel("Czas [s]")
    plt.title('Wplyw rozmiaru macierzy na czas')
    plt.grid(which='major')
    plt.grid(which='minor', linestyle=':')
    plt.savefig('./images/wykres.png', dpi=300)
    plt.show()
