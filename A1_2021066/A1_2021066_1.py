def rightAngle(n):
    for i in range(n):
        print(*[x for x in range(1, i + 2)], sep="")


def Isosceles(n):
    if n % 2 != 0:
        print("n must be even")
        return -1
    else:
        for i in range(n):
            print(" " * (n - i - 1), end="")
            print(*[x for x in range(1, i * 2 + 2)], sep="")


def Kite(n):
    if n % 2 != 0:
        print("n must be even")
        return -1
    else:
        for i in range(n):
            print(" " * (n - i - 1), end="")
            print(*[x for x in range(1, i * 2 + 2)], sep="")
        for i in range(n - 2, -1, -1):
            print(" " * (n - i - 1), end="")
            print(*[x for x in range(1, i * 2 + 2)], sep="")


def halfKite(n):
    for i in range(n):
        print(*[x for x in range(1, i + 2)], sep="")
    for i in range(n - 2, -1, -1):
        print(*[x for x in range(1, i + 2)], sep="")


def X(n):
    if n % 2 != 0:
        print("n must be even")
        return -1
    else:
        for i in range(n - 1, -1, -1):
            print(" " * (n - i - 1), end="")
            print(*[x for x in range(1, i * 2 + 2)], sep="")
        for i in range(1, n):
            print(" " * (n - i - 1), end="")
            print(*[x for x in range(1, i * 2 + 2)], sep="")


# while True:
for i in range(1):
    print("Choose one of the following patterns.")
    print("1. Right Angled Triangle")
    print("2. Isosceles triangle")
    print("3. Kite")
    print("4. Half Kite")
    print("5. X")
    choice = int(input("Enter your choice:"))
    n = int(input("Enter depth of pattern:"))
    if choice == 1:
        rightAngle(n)
    elif choice == 2:
        Isosceles(n)
    elif choice == 3:
        Kite(n)
    elif choice == 4:
        halfKite(n)
    elif choice == 5:
        X(n)
    else:
        print("Wrong choice")
    while True:
        redo = input("Would you like to try again? (y/n)")
        if redo.lower() == "n":
            exit()
        elif redo.lower() == "y":
            break
        else:
            print("Wrong choice")
