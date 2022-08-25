class Stack:
    def __init__(self):
        self.l = []

    def Push(self, a):
        for x in a:
            if x in ["(", "{", "["]:
                self.l.append(x)
            else:
                if self.Pop(x) == False:
                    return False
        return self.check()


    def Pop(self, r):
        if not self.l:
            return False
        x = self.l.pop()
        if x == '(' and r != ")":
            return False
        elif x == '{' and r != "}":
            return False
        elif x == '[' and r != "]":
            return False

    def check(self):
        if not self.l:
            return True


s = input()
ab = Stack()
if ab.Push(s):
    print("YES")
else:
    print("NO")
