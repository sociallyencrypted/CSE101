a = int(input())
b = int(input())
c = int(input())
if a + b > c and b + c > a and c + a > b:
    if (a ** 2 + b ** 2) == c ** 2 or (b ** 2 + c ** 2) == a ** 2 or (c ** 2 + a ** 2) == b ** 2:
        print ("Right ",end='')
    if a == b and b == c:
        print ("Equilateral Triangle")
    elif a == b or b == c or c == a:
        print ("Isosceles Triangle")
    else:
        print ("Scalene Triangle")
else:
    print ("Not a triangle.")
