from datetime import datetime

userlist = {}


class BankAccount:
    def __init__(self, username, password, currentbal):
        self.username = username
        self.password = password
        self.currentbal = currentbal
        with open(f"{self.username}.txt", "w") as f:
            pass

    def authenticate(self):
        passw = input("Enter your secret password: ")
        if passw == self.password:
            return True
        else:
            return False

    def deposit(self, amount):
        trycount = 0
        try:
            while True:
                assert trycount < 3
                if self.authenticate():
                    break
                trycount += 1
            self.currentbal += amount
            with open(f"{self.username}.txt", "a") as f:
                f.write(
                    f"{datetime.now()} The amount of rupees {amount} has been added Current balance -> {self.currentbal}\n"
                )
        except AssertionError:
            print("Too many wrong attempts!")

    def withdraw(self, amount):
        trycount = 0
        try:
            while True:
                assert trycount < 3
                if self.authenticate():
                    break
                trycount += 1
            if self.currentbal < amount:
                print("Low balance!! Cannot be debited at this time!")
            else:
                self.currentbal -= amount
                with open(f"{self.username}.txt", "a") as f:
                    f.write(
                        f"{datetime.now()} The amount of rupees {amount} has been deducted Current balance -> {self.currentbal}\n"
                    )
        except AssertionError:
            print("Too many wrong attempts!")

    def bankStatement(self):
        trycount = 0
        try:
            while True:
                assert trycount < 3
                if self.authenticate():
                    break
                trycount += 1
            print("Hey {username}! Here's your recent transaction history:\n")
            with open(f"{self.username}.txt", "r") as f:
                for line in f.readlines():
                    print(line)
        except AssertionError:
            print("Too many wrong attempts!")


def repmenu():
    print("Select an optiion.")
    print("1. Deposit")
    print("2. Withdraw")
    print("3.Print Statement")


print("Welcome to the Bank of IIIT-D")
username = input("Enter username:")
password = input("Enter password:")
currentbal = int(input("Enter starting balance:"))
obj = BankAccount(username, password, currentbal)
while True:
    repmenu()
    choice = int(input("Enter: "))
    if choice == 1:
        bal = int(input("Enter amount to be added: "))
        obj.deposit(bal)
    if choice == 2:
        bal = int(input("Enter amount to be withdrawn: "))
        obj.withdraw(bal)
    if choice == 3:
        obj.bankStatement()
    yn = input("Do you want to continue? (Y/N): ")
    if yn == "N":
        break
