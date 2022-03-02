def getReverse(n):
    return int(str(n)[::-1])


def checkPalindrome(n):
    return int(str(n)[::-1]) == n


def checkNarcissistic(n):
    return n == sum([int(i) ** len(str(n)) for i in str(n)])


def findDigitSum(n):
    x = sum([int(i) for i in str(n)])
    if x // 10 != 0:
        return x + findDigitSum(x)
    else:
        return x


def findSquareDigitSum(n):
    x = sum([int(i) ** 2 for i in str(n)])
    if x // 10 != 0:
        return x + findSquareDigitSum(x)
    else:
        return x


while True:
    print("Choose one of the following patterns.")
    print("1. Get reverse number")
    print("2. Check if number is palindrome")
    print("3. Check if number is narcissistic")
    print("4. Find digit sum")
    print("5. Find square digit sum")
    print("6. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        n = int(input("Enter number:"))
        print(getReverse(n))
    elif choice == 2:
        n = int(input("Enter number:"))
        print(checkPalindrome(n))
    elif choice == 3:
        n = int(input("Enter number:"))
        print(checkNarcissistic(n))
    elif choice == 4:
        n = int(input("Enter number:"))
        print(findDigitSum(n))
    elif choice == 5:
        n = int(input("Enter number:"))
        print(findSquareDigitSum(n))
    elif choice == 6:
        exit()
    else:
        print("Wrong choice")
