l = [int(i) for i in input().split()]
r = int(input())
ansl = []
for i in range(1 << len(l)):
    if sum(b == "1" for b in bin(i)[2:]) == r:
        ans = []
        for j in range(len(l)):
            if i & (1 << j):
                ans.append(l[j])
        ansl.append(ans)
print(ansl)
