s = input()
s = [s[i] for i in range(len(s))]
r = sorted(s)
a = []
b = ""
for x in range(len(s)):
    a += s[x]
    while True:
        if a != []:
            if a[-1] == r[0]:
                b += a[-1]
                del a[-1]
                del r[0]
            else:
                break
print(b + "".join(a[::-1]))
