dic = {}

n = int(input())
for i in range(n):
    a, b = [int(x) for x in input().split()]
    if i == 0:
        lasta = a
        dic[lasta] = [a, b]
    elif a == lasta:
        dic[lasta].append(b)
    else:
        lasta = a
        dic[lasta] = [a, b]

z = [tuple(r) for r in dic.values()]
print(z)
