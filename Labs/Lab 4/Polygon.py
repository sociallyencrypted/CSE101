n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

ans = True    
    
for j in range(n):
    if sum(l[0:j])+sum(l[j+1:]) <= l[j]:
        ans = False
        
print(ans)