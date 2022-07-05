import numpy as np
import time
from matplotlib import pyplot as plt


class Langrange:
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

    def interpolation(self, distance):
        result = 0.0
        for i in range(len(self.__interpolated_data)):
            a = 1.0
            for j in range(len(self.__interpolated_data)):
                if i != j:
                    a *= ((distance - self.__interpolated_data[j][0]) /
                          (self.__interpolated_data[i][0] - self.__interpolated_data[j][0]))
            result += a * self.__interpolated_data[i][1]

        return result

    def langrangeInterpolation(self):
        # 520 / steps
        intervals = [104, 65, 52, 13]

        # print("Langrange Interpolation")
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
                for j in np.arange(float(self.__interpolated_data[0][0]),
                                   float(self.__interpolated_data[node_num - 1][0]) + 1, 11):
                    res = self.interpolation(int(j))
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

    def clear(self):
        self.__distance = []
        self.__interpolated_data = []
        self.__interpolated_height = []
        self.__distance_ref = []
        self.__height_ref = []
        self.__distance_to_train = []
        self.__height_to_train = []

    def createPlot(self, i):
        plt.title('Interpolacją Lagrange\'a, p=' + str(len(self.__interpolated_data)))
        plt.plot(self.__distance_ref, self.__height_ref, 'r.', label='pełne dane')
        plt.plot(self.__distance, self.__interpolated_height, color='blue', label='funkcja interpolująca')
        plt.plot(self.__distance_to_train, self.__height_to_train, 'g.', label='dane do interpolacji')
        plt.legend()
        plt.xlabel("Dystans [m]")
        plt.ylabel("Wysokosc [m]")
        plt.suptitle(self.__file_names[i])
        plt.grid()
        plt.savefig(
            './results/langrange/' + self.__file_names_split[i] + '_p=' + str(len(self.__interpolated_data)) + '.png',
            dpi=300)
        plt.show()
