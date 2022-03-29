class Queue:
    def __init__(self):
        self.l = []
        self.uniq = []

    def Push(self, x):
        if x in self.l:
            self.uniq.append(-1)
        else:
            self.uniq.append(x)
        self.l.append(x)

    def getUniq(self):
        if self.uniqisempty():
            return ("null")
        else:
            return self.uniq[-1]


    def uniqisempty(self):
        if self.uniq == []:
            return True


s = input()
a = Queue()
for ch in s:
    a.Push(ch)
print(a.getUniq())