noteList = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def noteCreate():
    f1 = open("scaleMajor.txt", "w")
    f2 = open("scaleMinor.txt", "w")
    for note in noteList:
        f1.write(majorNotes(note))
        f1.write("\n")
        f2.write(minorNotes(note))
        f2.write("\n")
    f1.flush()
    f1.close()
    f2.flush()
    f2.close()


def majorNotes(root):
    series = ["Root", "W", "W", "H", "W", "W", "W", "H"]
    l = []  # List that will contain all notes for the series
    i = noteList.index(root)
    l.append(root)
    suffix = ""
    for x in range(len(series[1:])):
        if series[1:][x] == "W":
            i += 2
        else:
            i += 1
        if i >= len(noteList):
            if i >= len(noteList) + noteList.index(root):
                l.append(noteList[i - len(noteList)] + "'")
            else:
                l.append(noteList[i - len(noteList)])
        else:
            l.append(noteList[i])

    return " ".join(l)


def minorNotes(root):
    series = ["Root", "W", "H", "W", "W", "H", "W", "W"]
    l = []  # List that will contain all notes for the series
    i = noteList.index(root)
    l.append(root)
    suffix = ""
    for x in range(len(series[1:])):
        if series[1:][x] == "W":
            i += 2
        else:
            i += 1
        if i >= len(noteList):
            if i >= len(noteList) + noteList.index(root):
                l.append(noteList[i - len(noteList)] + "'")
            else:
                l.append(noteList[i - len(noteList)])
        else:
            l.append(noteList[i])

    return " ".join(l)


noteCreate()  # initialise both files
while True:
    note = input("Enter a note: ").upper()
    if note not in noteList:
        print("Note not found, try again.")
    else:
        scale = input("Scale? (Minor/Major):").lower()
        if scale == "minor":
            f = open("scaleMinor.txt", "r")
        elif scale == "major":
            f = open("scaleMajor.txt", "r")
        else:
            print("Invalid scale, try again")
            continue
        for line in f.readlines():
            if line.split()[0] == note:
                print(line)
        choice = input("Continue? (y/n): ")
        if choice == "n":
            break
