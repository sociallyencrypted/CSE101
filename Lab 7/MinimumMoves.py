n = int(input())
l = [int(x) for x in input().split()]
l.sort()
if n % 2 == 0:
    count = 0
    r = (l[(n - 2) // 2] + l[n // 2]) // 2
    for x in range(n):
        if l[x] != r:
            count += 1
    print(count)
else:
    count = 0
    r = l[n // 2]
    for x in range(n):
        if l[x] != r:
            count += 1
    print(count)
