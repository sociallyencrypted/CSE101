l1 = list(input())
l2 = list(input())
b = True
if len(l1) == len(l2):
    while len(l1) != 0:
        x = 0
        r = l1[x]
        r1 = l2[x]
        if l1.count(l1[x]) == 1:
            del l1[x]
            del l2[x]
        else:
            while l1.count(r) != 0:
                if l2[l1.index(r)] == r1:
                    del l2[l1.index(r)]
                del l1[l1.index(r)]
        if len(l1) != len(l2):
            b = False
            break
if b:
    print("YES")
else:
    print("NO")
