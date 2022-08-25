def sort_attribute(objl, attrib):
    if attrib == 1:
        objl.sort(key=lambda x: x.firstname)
    elif attrib == 2:
        objl.sort(key=lambda x: x.lastname)
    elif attrib == 3:
        objl.sort(key=lambda x: x.age)
    print("Order:")
    for x in objl:
        print(x)


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __repr__(self):
        rep = f"{self.firstname} {self.lastname} {self.age}"
        return rep


while True:
    print("Welcome to the Application!")
    n = int(input("Enter the number of people to be enrolled: "))
    people = []
    for i in range(n):
        fname = input(f"Enter first name of person {i+1}: ")
        lname = input(f"Enter last name of person {i+1}: ")
        age = input(f"Enter age of person {i+1}: ")
        person = Person(fname, lname, age)
        people.append(person)

    m = int(input("Enter number of queries: "))
    for i in range(m):
        attrib = input("Enter attribute(firstname/lastname/age): ")
        if attrib == "firstname":
            sort_attribute(people, 1)
        elif attrib == "lastname":
            sort_attribute(people, 2)
        elif attrib == "age":
            sort_attribute(people, 3)
        else:
            print("Wrong Option")

    choice = input(
        "Thanks for using the Application, if you wish to restart, press “Y” else press “N” to exit: "
    )
    if choice == "N":
        break
