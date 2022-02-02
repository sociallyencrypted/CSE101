n = abs(int(input()))
count = 0
d_ = n ** (1 / 3)
d = int('{0:.0f}'.format(d_))
for i in range (1, d + 1):
    for j in range (1, d + 1):
        if (i ** 3) + (j ** 3) == n:
            count += 1
if count >= 2:
    print (True)
else:
    print (False)