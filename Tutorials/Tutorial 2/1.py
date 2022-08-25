'''Given a list of n integers and an integer x, we want to make every number in the list equal to x. 
In one step we can either increase or decrease an element in the list by 2. 
Find the minimum number of steps required to make every element in the list equal to x or tell if it is impossible to do so'''

n =  int(input("Enter n:"))
l=[]
for i in range (n):
    l.append(int(input(str("Enter "+str(i)+"th element:"))))
x = int(input("Enter x:"))

steps = 0
isDoable = True
for y in l:
    if (x - y) % 2 != 0:
        isDoable = False
    else:
        steps += abs(y-x)/2
if isDoable:
    print(int(steps), " steps required.")
else:
    print("Not doable")
