def isPossible(l):
    sum1=0
    sum2 = sum(l)
    for i in range(len(l)-1):
        sum1 += l[i]
        sum2 -= l[i]
        if sum1 == sum2:
            return (True)
    return (False)


l = []
n = int(input())
for i in range(n):
    a = int(input())
    l.append(a)

if (isPossible(l)):
    print("YES")
else:
    print("NO")