l = [i for i in input().split()]
n = int(input())
try:
    assert n in range(-len(l), len(l))
    print(l[n])
except:
    print(-1)
