class Stack:
    def __init__(self):
        self.l = []
        self.min = []

    def Push(self, x):
        self.l.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        else:
            r = self.min[-1]
            self.min.append(min(x, r))                                                                                                                         

    def Pop(self):
        if not self.isempty():
            self.l.pop()
        if not self.minisempty():
            self.min.pop()

    def getMin(self):
        if not self.minisempty():
            return self.min[-1]
        else:
            return -1


    def minisempty(self):
        if self.min == []:
            return True

    
    def isempty(self):
        if self.l == []:
            return True


n = int(input())
a = Stack()
for x in range(n):
    r = input()
    if "Push" in r:
        a.Push(int(r.split()[1]))
    elif "Min" in r:
        print(a.getMin())
    elif "Pop" in r:
        a.Pop()