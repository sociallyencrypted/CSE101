class Cuboid:
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def getVolume(self):
        return self.l * self.b * self.h

    def getTotalSurfaceArea(self):
        return 2 * (self.l * self.b + self.b * self.h + self.h * self.l)

    def hasSameVolume(self, c2):
        if self.getVolume() == c2.getVolume():
            return "YES"
        return "NO"


n = int(input())
cl = []
for _ in range(n):
    l, b, h = [int(i) for i in input().split()]
    cl.append(Cuboid(l, b, h))
q = int(input())
for x in range(q):
    r = [int(i) for i in input().split()]
    if r[0] == 1:
        print(cl[r[1]].getVolume())
    elif r[0] == 2:
        print(cl[r[1]].getTotalSurfaceArea())
    else:
        print(cl[r[1]].hasSameVolume(cl[r[2]]))
