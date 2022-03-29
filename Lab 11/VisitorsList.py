class Visitors:
    def __init__(self):
        self.visitorsList = []


    def addVisitors(self, nodes):
        self.visitorsList += nodes


    def endSession(self, N):
        if len(self.visitorsList) <= N:
            print ("No more visitors")
        else:
            self.visitorsList = self.visitorsList[N:]
            print (' '.join(self.visitorsList))


x = Visitors()
l = input().split()
x.addVisitors(l)
x.endSession(int(input()))