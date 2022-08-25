import cases


def function2(n):
    # calculate the nth fibonacci number using iteration
    num1 = 0
    num2 = 1
    for i in range(n):
        num1, num2 = num2, num1 + num2
    return num2


def testing():
    cases.generateData()
    finp = open("inputs.txt", "r")
    foutp = open("outputs.txt", "r")
    inlines = finp.readlines()
    outlines = foutp.readlines()
    check = True
    for ln in range(len(inlines)):
        if function2(int(inlines[ln])) != int(outlines[ln]):
            check = False
    if check:
        print("SUCCESS")
    else:
        print("FAILED")


testing()
