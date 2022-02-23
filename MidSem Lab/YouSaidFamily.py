s1 = input()
s2 = input()
x1 = set(list(s1))
x2 = set(list(s2))
x = x1-x2
for h in s1:
    if h in x:
        print(h, end='')
print()