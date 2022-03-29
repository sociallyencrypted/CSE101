class Convert:
    def __init__(self, meter):
        self.num = meter

    def convertToFeet(self):
        return self.num * 3.28

    def convertToYards(self):
        return self.num * 1.09


n = int(input())
c = Convert(n)
print(c.convertToFeet(), c.convertToYard())