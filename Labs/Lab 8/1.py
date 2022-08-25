def countNum(l, count):
    if l == []:
        return count
    else:
        count += 1
        del l[-1]
        return countNum(l, count)


l = input().split()
print(countNum(l, 0))
