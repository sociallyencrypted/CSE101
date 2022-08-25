n = int(input())
try:
    assert n >= 0
    print(n)
except AssertionError:
    print("Age can't be negative")
