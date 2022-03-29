class ReportCard:
    def __init__(self, sname, sid, smarks):
        self.sname = sname
        self.sid = sid
        self.smarks = smarks

    def getFinalMarks(self):
        try:
            return int(sum(self.smarks) / len(self.smarks))
        except ZeroDivisionError:
            return 0

    def getGrade(self):
        if self.getFinalMarks() > 90:
            return "A"
        elif self.getFinalMarks() > 80:
            return "B"
        elif self.getFinalMarks() > 70:
            return "C"
        else:
            return "D"


name = input()
sid = int(input())
l = [int(i) for i in input().split()]
obj = ReportCard(name, sid, l)
print(obj.sname, obj.sid, obj.getFinalMarks(), obj.getGrade())
