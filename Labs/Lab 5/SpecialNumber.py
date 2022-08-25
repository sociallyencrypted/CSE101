def sortAndFindIndex(l,n):
    l = sorted(l)
    if n < l[0]:
        return 0
    for i in range(len(l)):
        if l[i] == n or n in range(l[i-1],l[i]):
            return i
    if n > l[len(l)-1]:
        return len(l)


l = [int(i) for i in input().strip().split()]
n = int(input())
print(sortAndFindIndex(l,n))