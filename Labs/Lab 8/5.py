n = int(input())
l = [int(i) for i in input().split()]
d = int(input())
ansl = []
bl = False
for r in range(len(l)):
    for i in range(1 << len(l)):
        if sum(b == "1" for b in bin(i)[2:]) == r:
            ans = []
            ans2 = []
            for j in range(len(l)):
                if i & (1 << j):
                    ans.append(l[j])
            if ans in ansl:
                break
            for x in l:
                if x not in ans:
                    ans2.append(x)
            ansl.append(ans)
            ansl.append(ans2)
            if abs(sum(ans) - sum(ans2)) == abs(d):
                bl = True
if bl:
    print("YES")
else:
    print("NO")
