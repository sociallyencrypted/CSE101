l = [int(x) for x in input().split()]
l1 = []
for i in range(len(l)):
    print(max(l[: i + 1]), end=" ")
