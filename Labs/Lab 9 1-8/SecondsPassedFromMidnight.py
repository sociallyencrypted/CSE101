h = int(input())
m = int(input())
try:
    assert h in range(24)
    assert m in range(60)
    print((3600 * h) + (60 * m))
except:
    print("Invalid")
