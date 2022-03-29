class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printp(self):
        print(self.x)
        print(self.y)

    def dist(self, p2):
        return (((self.x - p2.x) ** 2) + ((self.y - p2.y) ** 2)) ** (0.5)


x, y = [int(i) for i in input().split()]
p1 = Point(x, y)
x, y = [int(i) for i in input().split()]
p2 = Point(x, y)
p1.printp()
print(p1.dist(p2))
