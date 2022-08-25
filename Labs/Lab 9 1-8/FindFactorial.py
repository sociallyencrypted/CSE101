import math


n = int(input())
for i in range(n):
    try:
        x = int(input())
        try:
            assert x >= 0
            print(math.factorial(x))
        except AssertionError:
            print("Invalid Operation")
    except ValueError:
        print("Invalid Operation")
