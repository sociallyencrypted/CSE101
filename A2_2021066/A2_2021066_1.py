wordsDict = {}


def initDict():
    with open("question1_input.txt", "r+") as f:
        for line in f.readlines():
            wordList = [i for i in line.strip().split()]
            for words in wordList:
                if words not in wordsDict.keys():
                    wordsDict[words] = 1
                else:
                    wordsDict[words] += 1


def specWordCount():
    word = input("Enter word:")
    if word in wordsDict.keys():
        print("No. of occurences:", wordsDict[word])
    else:
        print("Word does not exist.")


def uniqueWords():
    for i in wordsDict.keys():
        print(i, end=" ; ")
    print()


def wordCount():
    for i in wordsDict.keys():
        print(i, ":", wordsDict[i])


def replaceWord():
    with open("question1_input.txt", "r+") as f:
        word1 = input("Enter word which has to be replaced:")
        if word1 in wordsDict.keys():
            word2 = input("Enter word to be replaced with:")
            """if word2 in wordsDict.keys():
                wordsDict[word2] += wordsDict[word1]
                del wordsDict[word1]
            else:
                wordsDict[word2] = wordsDict[word1]
                del wordsDict[word1]"""
            del wordsDict[word1]
            filedata = f.readlines()
            a = []
            for line in filedata:
                line1 = line.replace(word1, word2)
                a.append(line1)
            print(a)
            f.seek(0)
            f.write("".join(a))
        else:
            print("Word does not exist.")


while True:
    initDict()
    print("-" * 100)
    print("Enter your choice:")
    print(
        """1. Display specific Word Count
2. Display Unique Words
3. Display all Word Counts
4. Replace Word
5. Quit"""
    )
    choice = int(input())
    if choice == 1:
        specWordCount()
    elif choice == 2:
        uniqueWords()
    elif choice == 3:
        wordCount()
    elif choice == 4:
        replaceWord()
    elif choice == 5:
        exit()
    else:
        print("Invaid choice")
