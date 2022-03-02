def normalise(v):
    """normalise a vector v into a unit vector"""
    m = val(v)
    for i in range(3):
        v[i] /= m
    return v


def dot(v1, v2):
    """Calculate the dot product of vector v1 and vector v2"""
    pr = 0
    for i in range(3):
        pr += v1[i] * v2[i]
    return pr


def vectorSub(v1, v2):
    """Subtract vector v2 from vector v1"""
    vSub = []
    for i in range(3):
        vSub.append(v1[i] - v2[i])
    return vSub


def val(v):
    """Find the distance of a vector from origin"""
    add = 0
    for i in range(3):
        add += v[i] ** 2
    add = add**0.5
    return add


def addDis(s, v, d):
    """Add a distance s to vector v in direction d"""
    result = []
    for i in range(3):
        result.append(v[i] + (s * d[i] / val(d)))
    return result


def intersects(e, d, cen, r):
    """Find if ray intersects sphere, and if yes, prints the intersection points"""
    originToCenter = vectorSub(e, cen)
    d = normalise(d)
    a = 1
    b = 2 * dot(originToCenter, d)
    c = dot(originToCenter, originToCenter) - r * r
    disc = b * b - 4 * a * c  # Discriminant of Equation
    if disc > 0:
        t1 = (-b - (disc**0.5)) / (2 * a)
        t2 = (-b + (disc**0.5)) / (2 * a)
        if t1 > 0 or t2 > 0:
            print("Intersects")
            if t1 > 0:
                print(f"{t1=}")
                p1 = [round(num, 2) for num in addDis(t1, e, d)]
                print(p1)
            if t2 > 0:
                print(f"{t2=}")
                p2 = [round(num, 2) for num in addDis(t2, e, d)]
                print(p2)
        else:
            print("Does not intersect (ray ahead of sphere)")
    elif disc == 0:
        print("Tangent")
        t = (-b) / (2 * a)
        p = [round(num, 2) for num in addDis(t, e, d)]
        print(f"{t=}")
        print("Point of tangency is: ")
        print(p)
    else:
        print("Does not intersect")
    return disc > 0


print("Enter the origin of light, e, in vector form")
print("Seperate components with a space. For eg. if the vector is 1i+2j+3k enter 1 2 3")
e = [float(i) for i in input().split()]
print("Enter the direction of light, d, in vector form")
print("Seperate components with a space. For eg. if the vector is 1i+2j+3k enter 1 2 3")
d = [float(i) for i in input().split()]
x0 = float(input("Enter the X coordinate of the center of the sphere: "))
y0 = float(input("Enter the Y coordinate of the center of the sphere: "))
z0 = float(input("Enter the Z coordinate of the center of the sphere: "))
c = [x0, y0, z0]  # Store center of sphere as a vector too to simplify calculations
r = float(input("Enter the radius of the sphere: "))
intersects(e, d, c, r)
