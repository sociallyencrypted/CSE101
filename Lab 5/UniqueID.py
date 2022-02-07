n = 0


def identify(listOfNames):
    for i in range(len(listOfNames)):
        if len(listOfNames[i]) < n:
            listOfNames[i] = listOfNames[i] + str(i+1)
        else:
            listOfNames[i] = listOfNames[i][:n] + str(i+1)
    return listOfNames

l = [i for i in input().strip().split()]
n = int(input())
print(*identify(l), sep = ' ')
