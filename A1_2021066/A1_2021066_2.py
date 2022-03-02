def Shape2D():
    while True:
        print("Choose one of the following shapes.")
        print("1. Square")
        print("2. Rectangle")
        print("3. Rhombus")
        print("4. Parallelogram")
        print("5. Circle")
        choice = int(input("Enter choice: "))
        if choice == 1:
            s = float(input("Enter side: "))
            print("Perimeter:", round(4 * s, 2))
            print("Area:", round(s**2, 2))
            break
        elif choice == 2:
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            print("Perimeter:", round(2 * (l + b), 2))
            print("Area:", round(l * b, 2))
            break
        elif choice == 3:
            s = float(input("Enter side: "))
            d1 = float(input("Enter diagonal 1: "))
            d2 = float(input("Enter diagonal 2: "))
            print("Perimeter:", round(4 * s, 2))
            print("Area:", round(1 / 2 * d1 * d2, 2))
            break
        elif choice == 4:
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            h = float(input("Enter height: "))
            print("Perimeter:", round(2 * (l + b), 2))
            print("Area:", round(b * h, 2))
            break
        elif choice == 5:
            r = float(input("Enter radius: "))
            print("Perimeter: ", round(2 * 3.14 * r, 2))  # Assuming pi = 3.14
            print("Area: ", round(3.14 * r * r, 2))  # Assuming pi = 3.14
            break
        else:
            print("Wrong choice, try again.")


def Shape3D():
    while True:
        print("Choose one of the following shapes.")
        print("6. Cube")
        print("7. Cuboid")
        print("8. Right Circular Cone")
        print("9. Hemisphere")
        print("10. Sphere")
        print("11. Solid Cylinder")
        print("12. Hollow Cylinder")
        choice = int(input("Enter choice: "))
        if choice == 6:
            s = float(input("Enter side: "))
            print("CSA:", round(4 * s**2, 2))
            print("TSA:", round(6 * s**2, 2))
            print("Volume:", round(s**3, 2))
            break
        elif choice == 7:
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            h = float(input("Enter height: "))
            print("CSA:", round(2 * (l * h + b * h), 2))
            print("TSA:", round(2 * (l * b + b * h + h * l), 2))
            print("Volume:", round(l * b * h, 2))
            break
        elif choice == 8:
            l = float(input("Enter slant length: "))
            r = float(input("Enter radius: "))
            h = float(input("Enter height: "))
            print("CSA:", round(3.14 * (r * l), 2))  # Assuming pi = 3.14
            print("TSA:", round(3.14 * r * (r + l), 2))  # Assuming pi = 3.14
            print("Volume:", round(3.14 * 1 / 3 * r**2 * h, 2))  # Assuming pi = 3.14
            break
        elif choice == 9:
            r = float(input("Enter radius: "))
            print("CSA:", round(3.14 * 2 * r**2, 2))  # Assuming pi = 3.14
            print("TSA:", round(3.14 * 3 * r**2, 2))  # Assuming pi = 3.14
            print("Volume:", round(3.14 * 2 / 3 * r**3, 2))  # Assuming pi = 3.14
            break
        elif choice == 10:
            r = float(input("Enter radius: "))
            print("CSA:", round(3.14 * 4 * r**2, 2))  # Assuming pi = 3.14
            print("TSA:", round(3.14 * 4 * r**2, 2))  # Assuming pi = 3.14
            print("Volume:", round(3.14 * 4 / 3 * r**3, 2))  # Assuming pi = 3.14
            break
        elif choice == 11:
            r = float(input("Enter radius: "))
            h = float(input("Enter height: "))
            print("CSA:", round(3.14 * 2 * r * h, 2))  # Assuming pi = 3.14
            print("TSA:", round(3.14 * 2 * r * (r + h), 2))  # Assuming pi = 3.14
            print("Volume:", round(3.14 * r**2 * h, 2))  # Assuming pi = 3.14
            break
        elif choice == 12:
            r1 = float(input("Enter inner radius: "))
            r2 = float(input("Enter outer radius: "))
            h = float(input("Enter height: "))
            print("CSA:", round(3.14 * 2 * (r1 + r2) * h, 2))  # Assuming pi = 3.14
            print(
                "TSA:", round(3.14 * 2 * (r1 + r2) * (r2 - r1 + h), 2)
            )  # Assuming pi = 3.14
            print("Volume:", round(3.14 * (r2 - r1) ** 2 * h, 2))  # Assuming pi = 3.14
            break
        else:
            print("Wrong choice, try again.")


n = int(input("Enter number of students: "))
for _ in range(n):
    while True:
        shapeChoice = int(input("Enter 2 for 2D, 3 for 3D: "))
        if shapeChoice == 2:
            Shape2D()
            break
        elif shapeChoice == 3:
            Shape3D()
            break
        else:
            print("Wrong choice, try again.")
