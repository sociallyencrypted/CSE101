s = input()
indices = [int(i) for i in input().split()]
for x in range(len(indices)):
    try:
        print(s[indices[x]], end="")
    except IndexError:
        print("_", end="")
