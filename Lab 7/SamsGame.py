def allEqual(l):
    for x in l:
        if x[-1] != l[0][-1]:
            return False
    return True


def cn(lst):
    count = 0
    while True:
        if min(len(x) for x in lst) != 0:
            if allEqual(lst):
                for x in range(len(lst)):
                    lst[x] = lst[x][:-1]
                count += 1
            else:
                return count
        else:
            return count


lst = [x for x in input().split()]

if len(lst) == 1:
    print(len(lst[0]))

else:
    print(cn(lst))
