n = int(input())
if n == 1:
    print(0)
    exit()
grid = []
for j in range(n):
    l = [int(i) for i in input().strip().split()]
    if 0 in l:
        i = l.index(0)
        print(int(abs(j-((n-1)/2))+abs(i-((n-1)/2))))
        break