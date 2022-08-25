def findCommon(list1, list2):
    l= []
    for i in range(len(list1)):
        if list1[i] in list2:
            l.append(list1[i])
    return l


l1 = [i for i in input().strip().split()]
l2 = [i for i in input().strip().split()]
x = findCommon(l1, l2)
if len(x) == 0:
    print("No common students")
else:
    print(*x, sep=' ')
    print(len(x))