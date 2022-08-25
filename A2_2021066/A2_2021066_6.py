def matrixInput(n):
    mat = []
    for i in range(n):
        row = input(
            "Enter row " + str(i + 1) + " of matrix as space separated values: "
        ).split()
        mat.append(row)
    return mat


def printMenu():
    print()
    print("Choose an option:")
    print(
        """1) Normal traversal
2) Alternating traversal
3) Spiral traversal from outer to inwards
4) Boundary traversal
5) Diagonal traversal from right to left
6) Diagonal traversal from left to right
7) Exit"""
    )


def normal(n, matrix):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")


def alt(n, matrix):
    for i in range(n):
        for j in range(n):
            if i % 2 != 0:
                j = n - j - 1
            print(matrix[i][j], end=" ")


def boundary(n, matrix):
    for j in range(n):
        print(matrix[0][j], end=" ")
    for i in range(1, n):
        print(matrix[i][n - 1], end=" ")
    for j in range(n - 2, 0, -1):
        print(matrix[n - 1][j], end=" ")
    for i in range(n - 1, 0, -1):
        print(matrix[i][0], end=" ")


def spiral(n, matrix):
    for i in range(n):
        for x in range(i, n - i):
            print(matrix[i][x], end=" ")
            if n % 2 == 1 and i == (n // 2):
                return 0
        for x in range(i + 1, n - i):
            print(matrix[x][n - i - 1], end=" ")
        for x in range(n - i - 2, -1 + i, -1):
            print(matrix[n - i - 1][x], end=" ")
            if n % 2 == 0 and i == (n // 2 - 1):
                return 0
        for x in range(n - i - 2, i, -1):
            print(matrix[x][i], end=" ")


def diagonalLtoR(n, matrix):
    for x in range((2 * n) - 1):
        for i in range(n):
            for j in range(n):
                if (i + j) == x:
                    print(matrix[i][j], end=" ")


def diagonalRtoL(n, matrix):
    for x in range(-(n - 1), n):
        for i in range(n):
            for j in range(n):
                if (i - j) == x:
                    print(matrix[i][j], end=" ")


n = int(input("Enter n: "))
matrix = matrixInput(n)
while True:
    printMenu()
    choice = int(input("Enter choice: "))
    if choice == 1:
        normal(n, matrix)
    elif choice == 2:
        alt(n, matrix)
    elif choice == 3:
        spiral(n, matrix)
    elif choice == 4:
        boundary(n, matrix)
    elif choice == 5:
        diagonalLtoR(n, matrix)
    elif choice == 6:
        diagonalRtoL(n, matrix)
    elif choice == 7:
        exit()
    else:
        print("Invalid choice.")
