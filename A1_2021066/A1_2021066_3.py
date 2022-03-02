def calculate(degree, coefficients, lower, upper, step):
    values = []
    for i in range(lower, upper + 1, step):
        val = 0
        for j in range(degree + 1):
            val += coefficients[-j - 1] * (i**j)
        values.append(round(val))
    plot(values)


def plot(vals):
    minVal = min(vals)
    if minVal >= 0:
        for x in range(len(vals)):
            print("|", "*" * vals[x], sep="")
    else:
        for x in range(len(vals)):
            if vals[x] >= 0:
                print(" " * abs(minVal), "|", "*" * vals[x], sep="")
            else:
                print(" " * abs(minVal - vals[x]), "*" * abs(vals[x]), "|", sep="")


print("Provide Polynomial Function details: ")
deg = int(input("Enter the degree of the polynomial: "))
c = []
for i in range(1, deg + 2):
    c.append(float(input("coeff " + str(i) + ": ")))
lbound = int(input("Provide lower bound for x:"))
ubound = int(input("Provide higher bound for x:"))
incr = int(input("Provide the steps for which you wish to increment x:"))
calculate(deg, c, lbound, ubound, incr)
