class Lister:
    def __init__(self, l):
        self.l = l

    def find(self, a):
        for _ in range(len(self.l)):
            if self.l[_] < a:
                return self.l[_]
        return -1


n = int(input())
a = [int(i) for i in input().split()]
for i in range(n):
    x = a[i]
    obj = Lister(a[i:])
    print(obj.find(x), end=" ")
