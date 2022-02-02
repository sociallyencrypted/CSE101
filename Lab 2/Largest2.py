n =  int(input())
max1=0
max2=0
for i in range (n):
    a = int (input())
    if i == 0:
        max1 = a
    elif i == 1:
        max2 = a
    elif a>max1:
        max2=max1
        max1=a
    elif a>max2:
        max2=a
print (max1, max2)