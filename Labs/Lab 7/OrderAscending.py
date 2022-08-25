n = int(input())
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l = [x for x in l1]
l.sort()
l2.sort()
ln = []
for x in range(n):
    ln.append(l.index(l1[x]))
for i in range(n):
    print(l2[ln[i]], end=" ")
