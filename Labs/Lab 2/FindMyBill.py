n = int(input())
if n < 150:
    print(0)
elif n < 250:
    print((n-150)*10)
else:
    print((n-250)*15+1000)