charList = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)]  # global
specFormatsDict = {10: "Decimal", 2: "Binary", 8: "Octal", 16: "Hexadecimal"}  # global


def decimalToB(num, b):
    ans = []
    num = int(num)
    while num > 0:
        ans.append(charList[num % b])
        num //= b
    ans = ans[::-1]
    return ans


def AToDecimal(num, a):
    ans = 0
    for i in range(len(num)):
        ans += charList.index(num[i]) * (a ** (len(num) - i - 1))
    return ans


def inputFormat(a):
    inpStr = "Enter number in "
    if a in specFormatsDict.keys():
        inpStr += specFormatsDict[a]
        inpStr += ": "
    else:
        inpStr += "base "
        inpStr += str(a)
        inpStr += ": "
    number = input(inpStr).upper()
    if not set(number).issubset(set(charList[:a])):
        if a in specFormatsDict.keys():
            print("Entered number isn't", specFormatsDict[a])
        else:
            print("Entered number isn't base ", a)
    else:
        return number


def printFormat(num, b):
    outStr = "The number in "
    if b in specFormatsDict.keys():
        outStr += specFormatsDict[b]
        outStr += " is: "
        outStr += "".join(num)
    else:
        outStr += "base "
        outStr += str(b)
        outStr += " is: "
        outStr += "".join(num)
    print(outStr)


def menuPrint():
    print("-" * 100)
    print("NASA's Extraterrestrial Communications Tool")
    print("-" * 100)
    print("Select one of the options below:")
    print(
        """1. Convert Decimal to Binary
2. Convert Binary to Decimal
3. Convert Decimal to Hexadecimal
4. Convert Hexadecimal to Decimal
5. Convert Binary to Hexadecimal
6. Convert Hexadecimal to Binary
7. Convert Decimal to Octal
8. Convert Octal to Decimal
9. Convert Binary to Octal
10. Cinvert Octal to Binary
11. Convert Hexadecimal to Octal
12. Convert Octal to Hexadecimal
13. Custom Radix Conversion
14. Exit"""
    )


while True:
    menuPrint()
    choice = int(input("Enter choice: "))
    if choice == 1:
        number = inputFormat(10)
        printFormat(decimalToB(number, 2), 2)
    elif choice == 2:
        number = inputFormat(2)
        printFormat(AToDecimal(number, 2), 10)
    elif choice == 3:
        number = inputFormat(10)
        printFormat(decimalToB(number, 16), 16)
    elif choice == 4:
        number = inputFormat(16)
        printFormat(AToDecimal(number, 16), 10)
    elif choice == 5:
        number = inputFormat(2)
        printFormat(decimalToB(AToDecimal(number, 2), 16), 16)
    elif choice == 6:
        number = inputFormat(16)
        printFormat(decimalToB(AToDecimal(number, 16), 2), 2)
    elif choice == 7:
        number = inputFormat(10)
        printFormat(decimalToB(number, 8), 8)
    elif choice == 8:
        number = inputFormat(8)
        printFormat(AToDecimal(number, 8), 10)
    elif choice == 9:
        number = inputFormat(2)
        printFormat(decimalToB(AToDecimal(number, 2), 8), 8)
    elif choice == 10:
        number = inputFormat(8)
        printFormat(decimalToB(AToDecimal(number, 8), 2), 2)
    elif choice == 11:
        number = inputFormat(16)
        printFormat(decimalToB(AToDecimal(number, 16), 8), 8)
    elif choice == 12:
        number = inputFormat(8)
        printFormat(decimalToB(AToDecimal(number, 8), 16), 16)
    elif choice == 13:
        a = int(input("Enter radix A from which data is to be converted: "))
        b = int(input("Enter radix B to which data is to be converted: "))
        if a not in range(2, 37) or b not in range(2, 37):
            print("Out of bounds (2-37)")
        number = inputFormat(a)
        printFormat((decimalToB(AToDecimal(number, a), b)), b)
    elif choice == 14:
        exit()
    else:
        print("Invalid choice")
