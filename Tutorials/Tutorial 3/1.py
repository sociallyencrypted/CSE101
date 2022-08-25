'''Define a function maskify() which hides all but last four digits of your input string'''

def maskify(string):
    if len(string) > 4:
        return('#' * (len(string) - 4) + string[len(string) - 4:])
    else:
        return(string)

inpString = input("Enter a string:")
print(maskify(inpString))

