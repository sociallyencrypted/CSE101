from A3_2021066_1 import matMul, scale, translate, rotate, makem2
import numpy
import warnings
import random
import math

warnings.filterwarnings(
    "ignore", category=DeprecationWarning
)  # We're using numpy's matrix multiplier, hence we need to suppress deprecation warnings


def test_matmul(A, B, true_C):
    try:
        r = matMul(A, B)
        row = len(r)
        col = len(r[0])
        assert all([true_c[i][j] == r[i][j] for i in range(row) for j in range(col)])
        return True
    except AssertionError:
        return False


def test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z):
    try:
        r = scale(x, y, z, sx, sy, sz)
        true = [true_x, true_y, true_z]
        row = len(r)
        col = len(r[0])
        assert all([true[i][j] == r[i][j] for i in range(row) for j in range(col)])
        return True
    except AssertionError:
        return False


def test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z):
    try:
        r = translate(x, y, z, tx, ty, tz)
        true = [true_x, true_y, true_z]
        row = len(r)
        col = len(r[0])
        assert all([true[i][j] == r[i][j] for i in range(row) for j in range(col)])
        return True
    except AssertionError:
        return False


def test_rotate(x, y, z, axis, phi, true_x, true_y, true_z):
    try:
        r = rotate(x, y, z, axis, phi)
        true = [true_x, true_y, true_z]
        row = len(r)
        col = len(r[0])
        assert all(
            [
                round(true[i][j], 2) == round(r[i][j], 2)
                for i in range(row)
                for j in range(col)
            ]
        )
        return True
    except AssertionError:
        return False


# Using Numpy to generate random testcases

for i in range(5):
    print(f"Running matMul test {i+1}: ", end="")
    a = numpy.random.random_integers(0, 10, (3, i + 1))
    b = numpy.random.random_integers(0, 10, (i + 1, 3))
    true_c = numpy.matmul(a, b)
    # print(a, b, true_c, sep="\n")
    print(test_matmul(a, b, true_c))

for i in range(5):
    print(f"Running scale test {i+1}: ", end="")
    r = numpy.random.random_integers(0, 10, (3, 3))
    x = list(r[0])
    y = list(r[1])
    z = list(r[2])
    sx = random.randint(1, 10)
    sy = random.randint(1, 10)
    sz = random.randint(1, 10)
    scaled = [[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]]
    m2 = makem2(x, y, z)
    true_x = numpy.matmul(scaled, m2)[0]
    true_y = numpy.matmul(scaled, m2)[1]
    true_z = numpy.matmul(scaled, m2)[2]
    print(test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z))

for i in range(5):
    print(f"Running translate test {i+1}: ", end="")
    r = numpy.random.random_integers(0, 10, (3, 3))
    x = list(r[0])
    y = list(r[1])
    z = list(r[2])
    tx = random.randint(1, 10)
    ty = random.randint(1, 10)
    tz = random.randint(1, 10)
    translated = [[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz], [0, 0, 0, 1]]
    m2 = makem2(x, y, z)
    true_x = numpy.matmul(translated, m2)[0]
    true_y = numpy.matmul(translated, m2)[1]
    true_z = numpy.matmul(translated, m2)[2]
    print(test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z))

for i in range(3):
    for r in range(3):
        print(f"Running rotate test {r+1}: ", end="")
        axes = ["x", "y", "z"]
        axis = axes[i]
        print(f"Axis {axis}: ", end="")
        r = numpy.random.random_integers(0, 10, (3, 3))
        x = list(r[0])
        y = list(r[1])
        z = list(r[2])
        phi = random.randint(1, 360)
        phi1 = phi / 180 * math.pi
        s = math.sin(phi1)
        c = math.cos(phi1)
        if axis == "z":
            rotated = [[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        elif axis == "x":
            rotated = [[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]]
        elif axis == "y":
            rotated = [[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 1]]
        m2 = makem2(x, y, z)
        true_x = numpy.matmul(rotated, m2)[0]
        true_y = numpy.matmul(rotated, m2)[1]
        true_z = numpy.matmul(rotated, m2)[2]
        print(test_rotate(x, y, z, axis, phi, true_x, true_y, true_z))
