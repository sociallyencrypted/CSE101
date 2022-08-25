class Stack:
    def __init__(self):
        self.l = []
        self.sum1 = 0

    def Push(self, a):
        for x in a:
            if x in ["(", "{", "["]:
                self.l.append(x)
            else:
                if self.Pop(x) == False:
                    self.sum1 += 1

    def Pop(self, r):
        if not self.l:
            return False
        x = self.l.pop()
        if x == "(" and r != ")":
            return False
        elif x == "{" and r != "}":
            return False
        elif x == "[" and r != "]":
            return False
        else:
            return True

    def check(self):
        if not self.l:
            return True


s = input()
ab = Stack()
ab.Push(s)
print(ab.sum1 + len(ab.l))
