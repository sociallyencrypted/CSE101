def func(a,x):
    f = False
    l = []
    for i in range(len(a)):
        for j in range(len(a)):
            if [i, j] in l or [j, i] in l:
                continue
            l.append([i, j])
            if a[i] + a[j] == x:
                print(f"At {i=} and {j=}")
                if f:
                    print("f found true")
                    f = False
                    return f
                else:
                    f = True
    return f

n = int(input())
a = [int(i) for i in input().strip().split()]
x = int(input())



print(func(a,x))