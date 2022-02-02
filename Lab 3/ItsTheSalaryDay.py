def calculateGrossSalary(basic):
    if basic <= 10000:
        sum = (20 / 100) * basic
    elif (basic <= 20000):
        sum = (40 / 100) * basic
    else:
        sum = (60 / 100) * basic
    string="{salary:.2f}"
    print(string.format(salary = basic + sum))
    
sal = float(input())
calculateGrossSalary(sal)