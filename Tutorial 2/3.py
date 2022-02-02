'''Q3: Given a list of n integers, find the sum of the elements of the list excluding the segments that 
starts with 10 and ends with 20 (if there are multiple segments choose the largest).'''

n =  int(input("Enter n:"))
l=[]
sum1=0
sum2=0
x = False
for i in range (n):
    l.append(int(input(str("Enter "+str(i)+"th element:"))))
    sum1 += l[i]
try:
    a = l.index(10)
except ValueError:
    a = 0
try:
    b = l.index(20)
except ValueError:
    b = 0
if a and b:
    for j in range(a,b+1):
        sum2 += l[j]

print(sum1 - sum2)