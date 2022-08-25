def is_perfect(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    if (n == sum):
        print("Perfect")
    else:
        print("Not Perfect")

n = int(input())
is_perfect(n)