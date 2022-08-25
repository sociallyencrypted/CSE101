import math

def num_years(a0,p,n,t):
    time = 0
    a = a0
    while (a < t):
        a = math.floor(a * (p / 100) + a + n)
        time += 1
    return(time)

a0 = int(input())
p = float(input())
n = int(input())
t = int(input())
print(num_years(a0,p,n,t))