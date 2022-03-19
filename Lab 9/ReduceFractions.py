def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a, b = [int(i) for i in input().split()]
while True:
    try:
        x = gcd(a, b)
        assert x != 1
        a = a // x
        b = b // x
    except AssertionError:
        print(a, b)
        break
