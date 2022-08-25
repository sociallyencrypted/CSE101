class BST:
    def __init__(self, val):
        self.node = val
        self.l = None
        self.r = None

    def insert(self, val):
        if val == self.node:
            return
        elif val < self.node:
            if self.l == None:
                self.l = BST(val)
            else:
                self.l.insert(val)
        else:
            if self.r == None:
                self.r = BST(val)
            else:
                self.r.insert(val)

    def ispresent(self, val):
        if val == self.node:
            return True
        elif val > self.node:
            if self.r is None:
                return False
            else:
                return self.r.ispresent()
        elif val < self.node:
            if self.l is None:
                return False
            else:
                return self.l.ispresent()


a = BST(45)
a.printSubTrees()
