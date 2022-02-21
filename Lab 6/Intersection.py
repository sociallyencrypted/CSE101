def findDistance(a, b, c, d):
    return (((a - b) ** 2) + ((c - d) ** 2)) ** 0.5


x1, y1, r1 = map(float, input().split())
x2, y2, r2 = map(float, input().split())

if findDistance(x1, x2, y1, y2) <= r1 + r2:
    if (r1 > r2 and findDistance(x1, x2, y1, y2) + r2 < r1) or (
        r2 > r1 and findDistance(x1, x2, y1, y2) + r1 < r2
    ):
        print(False)
    else:
        print(True)
else:
    print(False)
