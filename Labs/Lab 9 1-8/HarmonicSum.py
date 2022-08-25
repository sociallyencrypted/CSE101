l = [int(i) for i in input().split()]
sumh = 0
for x in l:
    try:
        sumh += 1 / x
    except ZeroDivisionError:
        sumh += 0
try:
    print(round(len(l) / sumh, 1))
except ZeroDivisionError:
    print(0.0)
