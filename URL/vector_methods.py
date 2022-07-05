def vector_zeros(len):
    vector = []
    for _ in range(len):
        vector.append(0)
    return vector


def vector_ones(len):
    vector = []
    for _ in range(len):
        vector.append(1.0)
    return vector


def diagonal(a):
    diag = []
    for i in range(len(a)):
        diag.append(a[i][i])
    return diag


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


def vector_add_vector(a, b):
    tmp = copy_vector(a)
    for i in range(len(tmp)):
        tmp[i] += b[i]
    return tmp


def norm(vector):
    count = 0
    for el in vector:
        count += el ** 2
    return count ** 0.5

def vector_multiply_number(a, b):
    vector = []
    for i in range(len(a)):
        vector.append(a[i] * b)
    return vector