l1 = [i for i in input().strip().split()]
l2 = [i for i in input().strip().split()]
for i in range(len(l1)):
    print(i+1,'. ', sep='', end='')
    print(l1[i],l2[i])
