n = int(input())
s = int(input())
if n < 4:
    print(int(s*5/100))
elif n < 8:
    print(int(s*10/100))
else:
    print(int(s*15/100))