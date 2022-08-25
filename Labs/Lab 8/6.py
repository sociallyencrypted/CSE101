def twoSmallest(l, m, n, count):
    if count == len(l):
        return [m, n]
    if count == 0:
        if l[0] < l[1]:
            m = l[0]
            n = l[1]
        else:
            n = l[0]
            m = l[1]
    else:
        if l[count] < m:
            n = m
            m = l[count]
        elif l[count] < n:
            n = l[count]

    return twoSmallest(l, m, n, count + 1)


l = [int(i) for i in input().split()]
print(twoSmallest(l, 0, 0, 0))
