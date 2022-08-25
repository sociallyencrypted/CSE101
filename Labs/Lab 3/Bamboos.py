def findMinimumCoins(l):
    l.sort()
    index = int(n/2)
    y = l[index]
    coins = 0
    for x in l:
        coins += abs(y - x)
    print(coins)

l = []
n = int(input())
for i in range(n):
    a = int(input())
    l.append(a)

findMinimumCoins(l)

