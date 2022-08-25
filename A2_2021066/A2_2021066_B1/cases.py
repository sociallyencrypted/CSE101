def function1(count, num1, num2):
    # calculate the nth fibonacci number using recursion
    if count == 0:
        return num2
    else:
        return function1(count - 1, num2, num1 + num2)


def generateData():
    n = int(
        input("Enter the number of input-output pairs you would like to generate: ")
    )
    fin = open("inputs.txt", "w")
    fout = open("outputs.txt", "w")
    print(
        "This program calculates the nth fibonacci number. function1 does it using recursion, while function2 does it using iteration."
    )
    for i in range(n):
        num = input("Enter test case " + str(i + 1) + ": ")
        fin.write(str(num) + "\n")
    fin.flush()
    fin.close()
    with open("inputs.txt", "r") as f:
        x = f.readlines()
        for i in range(n):
            ans = function1(int(x[i]), 0, 1)
            fout.write(str(ans) + "\n")
    fout.flush()
    fout.close()
