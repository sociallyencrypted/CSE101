class Vector:
    def __init__(self, X):
        self.X = X

    def L1(self):
        sum1 = 0
        for x in range (len(self.X)):
            sum1 += abs(self.X[x])
        return int(sum1)

    def L2(self):
        sum1 = 0
        for x in range (len(self.X)):
            sum1 += abs(self.X[x]) ** 2
        return int(sum1 ** (0.5))

    def L_Infinity(self):
        return max([abs(x) for x in self.X])


k = int(input())
for _ in range(k):
    a  = [int(i) for i in input().split()]
    obj = Vector(a)
    print(obj. L1(), obj.L2(), obj.L_Infinity())
