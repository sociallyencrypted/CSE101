class Stack:
    def __init__(self):
        self.l = []
        self.top = 0

    def peek(self):
        return self.l[self.top]

    def push(self, element):
        self.l.append(element)
        self.top += 1

    def pop(self):
        if self.isempty():
            print("Error")
            return False
        else:
            self.top -= 1
            return self.l.pop()

    def isempty(self):
        return self.l == []

a = Stack()
