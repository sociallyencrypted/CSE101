d = int(input())
m = int(input())
if d in range(1,6):
    if m <= 120:
        print("YES")
    else:
        print("NO")
else:
    if m <= 240:
        print("YES")
    else:
        print("NO")