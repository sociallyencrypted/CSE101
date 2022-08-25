d = {}


def tribonacci(n):
    if n > 40:
        print("Number too large (>40)")
        exit()
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


n = int(input())
print(tribonacci(n))
