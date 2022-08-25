class Numbers:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def getArithmetic(self):
        return (self.a + self.b) / 2

    def getGeometric(self):
        return (self.a * self.b) ** 0.5

    def getHarmonic(self):
        return 2 / (1 / self.a + 1 / self.b)


a, b = [int(i) for i in input().split()]
x = Numbers(a, b)
print(x.getArithmetic(), x.getGeometric(), x.getHarmonic())
