def findCount(l):
    f = l[0][0]
    count = 0
    while (isValid(l,f)):
        count+=1
        x = []
        for i in l:
            if len(i) > 1:
                x.append(i[1:])
            else:
               return count
            l = x
            f = l[0][0]
    return count

def isValid(l,f):
    for i in l:
        if i[0]!=f:
            return False
    return True

l = [i for i in input().split()]
print(findCount(l))
    