'''Q2: Given a number N, print the whole Fibonacci sequence for N.
Sample Input:  
5
Sample Output:
0
1
1
2
3 '''

a = 0
b = 1
n = int(input("enter n:"))
print(a)
print(b)
for i in range(n-2):
    print(a + b)
    a, b = b, a + b