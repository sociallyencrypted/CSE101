students = {}  # Follows the format StudentNum: [StudentName, Marks]
answers = {}


def readStudents():
    studentInfoFile = open("Admin/RegisteredStudents.txt", "r")
    studentInfo = studentInfoFile.readlines()
    for i in studentInfo:
        l = i.split()
        studentNum = l[1]
        studentName = l[0]
        students[studentNum] = []
        students[studentNum].append(studentName)


def initAnswers():
    keyFile = open("Admin/AnswerKey.txt", "r")
    answerLines = [line.split() for line in keyFile.readlines()]
    for i in answerLines:
        answers[i[0]] = i[1]


def calculateMarks(studentNum):
    """Takes in the student number for which the marks are to be calculated, opens the corrosponding file, checks it against the answer key and returns the marks after calculating them"""
    fileName = "Student/" + students[studentNum][0] + "_" + studentNum + ".txt"
    examFile = open(fileName, "r")
    responseLines = [line.split() for line in examFile.readlines()]
    marks = 0
    for i in responseLines:
        if answers[i[0]] == i[1]:
            marks += 4
        elif i[1] == "-":
            marks += 0
        else:
            marks -= 1
    return marks


def writeFinalRep():
    reportFile = open("Admin/FinalReport.txt", "w")
    l = []
    for studentNum in students.keys():
        marks = calculateMarks(studentNum)
        students[studentNum].append(marks)
        writeStr = (
            students[studentNum][0]
            + " "
            + studentNum
            + " "
            + str(students[studentNum][1])
            + "\n"
        )
        l.append(writeStr)
    reportFile.writelines(l)


initAnswers()
readStudents()
writeFinalRep()
