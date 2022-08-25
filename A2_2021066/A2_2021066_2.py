import math


def readQueries():
    n = int(input("Enter n:"))
    x = [float(i) for i in input("Enter x as space seperated integers:").split()]
    y = [float(i) for i in input("Enter y as space seperated integers:").split()]
    z = [float(i) for i in input("Enter z as space seperated integers:").split()]
    q = int(input("Enter q:"))
    queries = []
    for i in range(q):
        queries.append(input("Enter query:"))
    return (n, x, y, z, q, queries)


def writeList(m):
    with open("ansLists.txt", "w") as r:
        r.write(" ".join([str(x) for x in m[0]]))
        r.write("\n")
        r.write(" ".join([str(x) for x in m[1]]))
        r.write("\n")
        r.write(" ".join([str(x) for x in m[2]]))
        r.write("\n")
        r.flush()
        r.close()


def writeQueries(x, y, z):
    with open("queries.txt", "w") as s:
        s.write(" ".join([str(i) for i in x]))
        s.write("\n")
        s.write(" ".join([str(i) for i in y]))
        s.write("\n")
        s.write(" ".join([str(i) for i in z]))
        s.flush()
        s.close()


def matrixMul(n, m1, m2):
    """Variables in this function with a suffix 1 indicate the variable is related to m1, those with a suffix 2 are related to m2, and those without any suffix are related to the final result."""
    l = [[], [], [], []]  # This list stores the final answer
    for j2 in range(n):
        col_j = [0, 0, 0, 0]  # jth columnt of result matrix
        for i2 in range(4):
            for i1 in range(4):
                col_j[i1] += m1[i1][i2] * m2[i2][j2]
        for i in range(4):
            l[i].append(round(col_j[i], 2))
    return l


def transformMatrix(query):
    matrix = []
    if query[0] == "S":
        sx = float(query[1])
        sy = float(query[2])
        sz = float(query[3])
        matrix = [[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]]
    elif query[0] == "T":
        tx = float(query[1])
        ty = float(query[2])
        tz = float(query[3])
        matrix = [[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz], [0, 0, 0, 1]]
    elif query[0] == "R":
        axis = query[1]
        phi = float(query[2]) / 180 * math.pi
        s = math.sin(phi)
        c = math.cos(phi)
        if axis == "z":
            matrix = [[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        elif axis == "x":
            matrix = [[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]]
        elif axis == "y":
            matrix = [[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 1]]
    return matrix


n, x, y, z, q, queries = readQueries()
writeQueries(x, y, z)
m2 = [x, y, z]
m2.append([1] * n)
for i in range(q):
    query = queries[i]
    m1 = transformMatrix(query.strip().split())
    m2 = matrixMul(n, m1, m2)
writeList(m2)
