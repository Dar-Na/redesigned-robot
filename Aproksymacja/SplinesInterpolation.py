import numpy as np
import time
from matplotlib import pyplot as plt
from Matrix import *


class Splines:
    __file_names = []
    __file_names_split = []
    __data = []
    __distance = []
    __interpolated_data = []
    __interpolated_height = []
    __distance_ref = []
    __height_ref = []
    __distance_to_train = []
    __height_to_train = []

    def __init__(self, data, filenames):
        self.__data = data
        self.__file_names = filenames
        for f in filenames:
            index = f.index('.')
            self.__file_names_split.append(f[0:index])

    def splinesInterpolation(self):
        # 520 / steps
        intervals = [104, 65, 52, 13]

        # print("Splines Interpolation")
        for i in range(len(self.__data)):
            # print(str(self.__file_names_split[i]))
            for interval in range(len(intervals)):
                self.clear()
                step = intervals[interval]
                node_num = int(520 / step)

                k = 0
                for g in range(node_num):
                    x, y = self.__data[i][k]
                    self.__interpolated_data.append([float(x), float(y)])
                    k += step

                # time0 = time.time()
                result = self.splines()
                for j in np.arange(float(self.__interpolated_data[0][0]),
                                   float(self.__interpolated_data[node_num - 1][0]) + 1, 11):
                    res = self.interpolate(j, result)
                    self.__distance.append(j)
                    self.__interpolated_height.append(res)
                # print('nodes: ', str(len(self.__interpolated_data)), 'time:', time.time() - time0)

                for j in self.__data[i]:
                    if float(j[0]) <= self.__distance[len(self.__distance) - 1]:
                        self.__distance_ref.append(float(j[0]))
                        self.__height_ref.append(float(j[1]))

                for data in self.__interpolated_data:
                    self.__distance_to_train.append(data[0])
                    self.__height_to_train.append(data[1])

                self.createPlot(i)
            # print()

    def interpolate(self, distance, x):
        result = 0
        for i in range(len(self.__interpolated_data) - 1):
            result = 0
            if self.__interpolated_data[i][0] <= distance <= self.__interpolated_data[i + 1][0]:
                for j in range(4):
                    h = distance - self.__interpolated_data[i][0]
                    # ai + bi * h + ci * h^2 + di * h^3
                    result += x[4 * i + j] * pow(h, j)
                break

        return result

    def splines(self):
        nodes_number = len(self.__interpolated_data)
        N = 4 * (nodes_number - 1)
        A = create_matrix(N, 0, 0, 0)
        b = vector_zeros(N)

        # S0(x0) = f(x0) = [1 * a0] + [0 * b0] + [0 * c0] + [0 * d0] + [0 * a1] + ... = [1 * a0] = f(x0)
        A[0][0] = 1
        b[0] = self.__interpolated_data[0][1]

        # S0(x1) = f(x1) = [1 * a0] + [h * b0] + [h^2 * c0] + [h^3 * d0] =  [1 * a0] = f(x1)
        h = self.__interpolated_data[1][0] - self.__interpolated_data[0][0]
        A[1][0] = 1
        A[1][1] = h
        A[1][2] = pow(h, 2)
        A[1][3] = pow(h, 3)
        b[1] = self.__interpolated_data[1][1]

        # S''0(x0) = 0 = [1 * c0] = 0
        A[2][2] = 1

        # S''n-1(xn) = 0 = [2 * cn-1 * 1] + [6 * dn-1 * h] = 0
        h = self.__interpolated_data[nodes_number - 1][0] - self.__interpolated_data[nodes_number - 2][0]
        A[3][4 * (nodes_number - 2) + 2] = 2
        A[3][4 * (nodes_number - 2) + 3] = 6 * h

        for i in range(1, nodes_number - 1):
            h = self.__interpolated_data[i][0] - self.__interpolated_data[i - 1][0]

            # Si(xi) = f(xi) = [ai * 1] = f(xi)
            A[4 * i][4 * i] = 1
            b[4 * i] = self.__interpolated_data[i][1]

            # Si(xi+1) = f(x+1) = [1 * ai] + [h * bi] + [h^2 * ci] + [h^3 * di] = f(xi+1)
            A[4 * i + 1][4 * i] = 1
            A[4 * i + 1][4 * i + 1] = h
            A[4 * i + 1][4 * i + 2] = pow(h, 2)
            A[4 * i + 1][4 * i + 3] = pow(h, 3)
            b[4 * i + 1] = self.__interpolated_data[i + 1][1]

            # S'i-1(xi) = S'i(xi) =
            # [1 * bi-1] + [2 * h * ci-1] + [3 * h^2 * di-1] = [bi] = 0
            A[4 * i + 2][4 * (i - 1) + 1] = 1
            A[4 * i + 2][4 * (i - 1) + 2] = 2 * h
            A[4 * i + 2][4 * (i - 1) + 3] = 3 * pow(h, 2)
            A[4 * i + 2][4 * i + 1] = -1
            b[4 * i + 2] = 0

            # S''i-1(xi) = S''i(xi) =
            # [2 * ci-1] + [6 * di-1 * h] = [2 * ci] + [6 * di * h] =
            # [2 * ci-1] + [6 * di-1 * h] = [2 * ci] = 0
            A[4 * i + 3][4 * (i - 1) + 2] = 2
            A[4 * i + 3][4 * (i - 1) + 3] = 6 * h
            A[4 * i + 3][4 * i + 2] = -2
            b[4 * i + 3] = 0

        x = factorization_LU(A, b, N)
        return x

    def clear(self):
        self.__distance = []
        self.__interpolated_data = []
        self.__interpolated_height = []
        self.__distance_ref = []
        self.__height_ref = []
        self.__distance_to_train = []
        self.__height_to_train = []

    def createPlot(self, i):
        plt.title('Interpolacją Splinami, p=' + str(len(self.__interpolated_data)))
        plt.plot(self.__distance_ref, self.__height_ref, color='red', label='dane')
        plt.plot(self.__distance, self.__interpolated_height, color='blue', label='funkcja interpolująca')
        plt.plot(self.__distance_to_train, self.__height_to_train, 'o', color='green', label='dane do interpolacji')
        plt.legend()
        plt.xlabel("Dystans [m]")
        plt.ylabel("Wysokosc [m]")
        plt.suptitle(self.__file_names[i])
        plt.grid()
        plt.savefig(
            './results/splines/' + self.__file_names_split[i] + '_p=' + str(len(self.__interpolated_data)) + '.png',
            dpi=300)
        plt.show()