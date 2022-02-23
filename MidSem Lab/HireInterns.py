l = [int(i) for i in input().split()]
n = int(input())

avg_total = int(sum(l) / len(l))
l.sort()
print(l)
avg_best = int(sum(l[len(l) - n :]) / n)
dic = {"AVG_TOTAL": avg_total, "AVG_BEST": avg_best}
print(dic)
