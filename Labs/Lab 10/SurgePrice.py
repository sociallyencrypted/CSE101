class Metro:
    def __init__(self, line, currentfare) -> None:
        self.line = line
        self.currentfare = currentfare

    def surgePrice(self):
        if self.line == "Blue":
            surgedprice = 2 * self.currentfare
        else:
            surgedprice = 1.5 * self.currentfare
        return surgedprice


l = input()
cp = float(input())
metron = Metro(l, cp)
print(metron.surgePrice())
