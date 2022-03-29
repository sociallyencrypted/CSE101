class Queue:
    def __init__(self):
        self.list = []
        self.front = 0
        self. end = 0


    def add(self, node):
        self.list.append(node)
        self.end +=1


    def remove(self, node):
        if self.isempty():
            return None
        else:
            obj = self.qdata[self.front]
            self.front += 1
            return obj


    def isempty(self):
        if self.front == self.end:
            return True
        return False
    

    '''def __str__(self):
        s = ""
        for x in range (len(self)):
            s+=str(self.list[x])
            s+=" "
        return s'''


    def __len__(self):
        return self.end - self.front

    
    def __eq__(self, other):
        if self.list()[self.start:self.end+1]  == other.list()[other.start:other.end+1] :
            return True


x = Queue()
y=x
print(str(x))
y.add(1)
y.add(2)
print(x)
print(x is y)