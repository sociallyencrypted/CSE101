class Employee:
    def __init__(self, fname, lname):
        self.fullname = fname + " " + lname
        self.email = fname + "." + lname + "@company.com"
        self.fname = fname
        self.lname = lname


employees = {}
n, k = [int(i) for i in input().split()]
for _ in range(n):
    i, fname, lname = [i for i in input().split("-")]
    employees[i] = Employee(fname, lname)
for x in range(k):
    i, query = [i for i in input().split()]
    obj = employees[i]
    if query == "firstname":
        print(obj.fname)
    if query == "lastname":
        print(obj.lname)
    if query == "fullname":
        print(obj.fullname)
    if query == "email":
        print(obj.email)
