def calculate_area(l, a, b, d):
    if b < a:
        d = -d
    if (b - a) % d != 0:
        print("Error: b - a not divisible by d")
        exit()
    else:
        area_i = 0
        for i in range(a, b, d):
            area_i += d / 6 * (f(l, i) + 4 * f(l, i + d / 2) + f(l, i + d))
        return area_i


def f(l, x):
    val = 0
    for j in range(len(l)):
        val += x ** l[j]
    return val


l = [float(i) for i in input("Enter powers seperated by space: ").split()]
a = int(input("Enter a: "))
b = int(input("Enter b: "))
d = int(input("Enter d: "))
print(calculate_area(l, a, b, d))
