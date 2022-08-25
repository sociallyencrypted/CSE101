class Student:
    def __init__(self, name, cgpa, branch):
        self.isPlaced = False
        self.name = name
        self.cgpa = cgpa
        self.branch = branch

    def isEligible(self, company):
        if not self.isPlaced:
            if self.branch in company.branches:
                if self.cgpa >= company.requiredcgpa:
                    print(f"Student {self.name} is eligible for Company {company.name}")
                    return True
        print(f"Student {self.name} is not eligible for Company {company.name}")
        return False

    def apply(self, company):
        company.appliedStudents.append(self)

    def getsPlaced(self):
        self.isPlaced = True


class Company:
    def __init__(self, name, requiredcgpa, branches, positionOpen):
        self.appliedStudents = []
        self.name = name
        self.requiredcgpa = requiredcgpa
        self.branches = branches
        self.positionOpen = positionOpen
        self.applicationOpen = True

    def hireStudents(self):
        k = self.positionOpen
        self.appliedStudents.sort(key=lambda x: x.cgpa, reverse=True)
        if len(self.appliedStudents) < k:
            self.selected = self.appliedStudents
        else:
            self.selected = self.appliedStudents[:k]
        for student in self.selected:
            student.getsPlaced()
        print("Students Hired:", ", ".join([x.name for x in self.selected]))
        self.closeApplication()

    def closeApplication(self):
        self.applicationOpen = False
        print("No. of Positions Filled:", len(self.selected))


n = int(input("Enter number of students: "))
students = []
for i in range(n):
    while True:
        name = input(f"Enter name of student {i+1}: ")
        try:
            cgpa = float(input(f"Enter cgpa of student {i+1}: "))
            assert 0 <= cgpa <= 10
            try:
                branch = input(f"Enter branch of student {i+1}: ")
                assert branch in ["CSE", "CSAM", "ECE"]
                student = Student(name, cgpa, branch)
                students.append(student)
                break
            except AssertionError:
                print("Invalid Branch. Must be either CSE, ECE or CSAM")
        except AssertionError:
            print("CGPA out of bounds (0-10)")

m = int(input("Enter number of companies: "))
for i in range(m):
    while True:
        name = input(f"Enter name of company {i+1}: ")
        try:
            cgpa = float(input(f"Enter required cgpa at company {i+1}: "))
            assert 0 <= cgpa <= 10
            try:
                branches = input(
                    f"Enter space seperated branches accepted at company {i+1}: "
                ).split()
                for branch in branches:
                    assert branch in ["CSE", "CSAM", "ECE"]
                positions = int(
                    input(f"Enter number of positions open at company {i+1}: ")
                )
                company = Company(name, cgpa, branches, positions)
                for student in students:
                    if student.isEligible(company):
                        student.apply(company)
                company.hireStudents()
                break
            except AssertionError:
                print("Invalid Branch. Must be either CSE, ECE or CSAM")
        except AssertionError:
            print("CGPA out of bounds (0-10)")
