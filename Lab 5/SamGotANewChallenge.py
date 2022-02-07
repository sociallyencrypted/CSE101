def checkUnique(l):
    for i in range(len(l)):
        if l.count(l[i]) == 1:
            return i
    return -1


n = int(input())
l = [i for i in input().strip().split()]
print(checkUnique(l))

