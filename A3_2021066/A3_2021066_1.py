import math


def matMul(m1, m2):
    n = len(m1)
    m = len(m1[0])
    o = len(m2[0])
    """Variables in this function with a suffix 1 indicate the variable is related to m1, those with a suffix 2 are related to m2, and those without any suffix are related to the final result."""
    l = [[0] * o] * n  # This list stores the final answer
    x = []
    for j2 in range(o):
        col_j = [0] * n  # jth column of result matrix
        for i2 in range(m):
            for i1 in range(n):
                col_j[i1] += m1[i1][i2] * m2[i2][j2]
        x.append(col_j)
    l = [[x[j][i] for j in range(o)] for i in range(n)]
    return l


def makem2(x, y, z):
    m2 = [x, y, z]
    m2.append([1] * len(x))
    return m2


def translate(x, y, z, tx, ty, tz):
    m2 = makem2(x, y, z)
    matrix = [[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz], [0, 0, 0, 1]]
    mnew = matMul(matrix, m2)
    return mnew[:-1]


def scale(x, y, z, sx, sy, sz):
    m2 = makem2(x, y, z)
    matrix = [[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]]
    mnew = matMul(matrix, m2)
    return mnew[:-1]


def rotate(x, y, z, axis, phi):
    m2 = makem2(x, y, z)
    phi = phi / 180 * math.pi
    s = math.sin(phi)
    c = math.cos(phi)
    if axis == "z":
        matrix = [[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    elif axis == "x":
        matrix = [[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]]
    elif axis == "y":
        matrix = [[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 1]]
    mnew = matMul(matrix, m2)
    return mnew[:-1]
