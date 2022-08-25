idr = 1


class LaundryServices:
    def __init__(self, name, contact, email, ctype, branded, season):
        self.cprice = {"Cotton": 50, "Silk": 30, "Woolen": 90, "Polyester": 20}
        self.name = name
        self.contact = contact
        self.email = email
        self.ctype = ctype
        self.branded = branded
        self.season = season
        global idr
        self.id = idr
        idr += 1

    def customerDetails(self):
        print("Details:")
        print(f"Name: {self.name}")
        print(f"Contact: {self.contact}")
        print(f"Email: {self.email}")
        print(f"Types of Clothes: {self.ctype}")
        print(f"Branded?: {self.branded}")

    def calculateCharge(self):
        self.price = 0
        if self.season == "Winter":
            mul = 0.5
        else:
            mul = 2
        for i in range(len(self.ctype)):
            price = self.cprice[self.ctype[i]]
            price *= mul
            if self.branded[i]:
                price *= 1.5
            else:
                price *= 1
            self.price += price
        return self.price

    def finalDetails(self):
        self.customerDetails()
        self.calculateCharge()
        print(f"Total Charge: {self.calculateCharge()}")
        if self.price > 200:
            print("To be returned in 4 days!")
        else:
            print("To be returned in 7 days!")


while True:
    name = input("Name of customer: ")
    contact = int(input("Contact number: "))
    email = input("Email: ")
    clothes = []
    brand = []
    n = int(input("Number of clothes: "))
    typel = {1: "Cotton", 2: "Silk", 3: "Woolen", 4: "Polyester"}
    for i in range(n):
        ct = int(
            input(
                "Enter type of cloth (1 for Cotton, 2 for Silk, 3 for Woolen and 4 for Polyester)"
            )
        )
        clothes.append(typel[ct])
        branded = int(input("Is the cloth branded? Enter 1 for yes, 2 for no: "))
        brand.append(bool(branded))
    season = input("Season: ")
    obj = LaundryServices(name, contact, email, clothes, brand, season)
    obj.finalDetails()
    c = input("Continue? (Y/N): ")
    if c == "N":
        break
