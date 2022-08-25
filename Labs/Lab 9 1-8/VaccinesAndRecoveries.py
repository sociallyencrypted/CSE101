d = {}
df = {}


def tribonacci(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    else:
        if n - 1 in d.keys():
            a = d[n - 1]
        else:
            a = tribonacci(n - 1)
            d[n - 1] = a
        if n - 2 in d.keys():
            b = d[n - 2]
        else:
            b = tribonacci(n - 2)
            d[n - 2] = b
        if n - 3 in d.keys():
            c = d[n - 3]
        else:
            c = tribonacci(n - 3)
            d[n - 3] = c
        return a + b + c


def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        if n - 1 in df.keys():
            a = df[n - 1]
        else:
            a = fibonacci(n - 1)
            df[n - 1] = a
        if n - 2 in df.keys():
            b = df[n - 2]
        else:
            b = fibonacci(n - 2)
            df[n - 2] = b
        return a + b


n = int(input())
try:
    assert n > 0
    print(tribonacci(n) - fibonacci(n))
except AssertionError:
    print("Not possible")
