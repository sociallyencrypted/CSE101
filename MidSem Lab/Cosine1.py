def calculateCosine(x1, x2, x3, x4, y1, y2, y3, y4, z1, z2, z3, z4):
    a1 = x2 - x1
    a2 = x4 - x3
    b1 = y2 - y1
    b2 = y4 - y3
    c1 = z2 - z1
    c2 = z4 - z3
    cosA = abs(
        (a1 * a2 + b1 * b2 + c1 * c2)
        / (((a1**2 + b1**2 + c1**2) * (a2**2 + b2**2 + c2**2)) ** 0.5)
    )
    return cosA


x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
z = [int(i) for i in input().split()]
x1, x2, x3, x4 = x
y1, y2, y3, y4 = y
z1, z2, z3, z4 = z
print(calculateCosine(x1, x2, x3, x4, y1, y2, y3, y4, z1, z2, z3, z4))
