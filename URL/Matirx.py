from math import sin

class Matrix:
    def __init__(self, index):
        self.d = int(index % 10)
        index /= 10
        self.c = int(index % 10)
        index /= 10
        self.e = int(index % 10)
        index /= 10
        self.f = int(index % 10)
        self.N = int(900 + self.c * 10 + self.d)


    def create_matrix(self, a1, a2, a3):
        a = []
        for i in range(self.N):
            row = []
            for j in range(self.N):
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

    def create_matrix_a(self):
        return self.create_matrix(int(self.e + 5), -1, -1)

    def create_matrix_c(self):
        return self.create_matrix(3, -1, -1)

    def create_vector_b(self):
        b = []
        for i in range(self.N):
            b.append(sin(i * (self.f + 1)))
        return b
