def colour(l, p, q):
    g = [p, q]
    rep = [0, 0]
    l1 = l
    for i in range(len(l[0])):
        if i % 2 == 0:
            singer = "D"
        else:
            singer = "S"
        for j in range(len(l)):
            if 1 in l[j]:
                r = l[j].index(1)
                rep[i % 2] += (len(l) - j) * (g[i % 2] + i)
                for x in range(j, len(l)):
                    l1[x][r] = singer
                break
    return l1, rep


def prettyPrint(l):
    for line in l:
        for x in line:
            print(x, end="")
        print()


p, q = [int(i) for i in input().split()]
m, n = [int(i) for i in input().split()]
l = []
for i in range(m):
    line = [int(i) for i in input()]
    l.append(line)
print()
lColoured, reputation = colour(l, p, q)
print(reputation[0], reputation[1])
prettyPrint(lColoured)
