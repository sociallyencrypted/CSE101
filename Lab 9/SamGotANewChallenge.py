n = int(input())
for i in range(n):
    try:
        x = int(input())
        print("Integer")
    except ValueError:
        print("Not an Integer")
