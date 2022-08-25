l = []


def wordPermutations(string, i, length):
    if i == length:
        l.append("".join(string))
    else:
        for j in range(i, length):
            string[i], string[j] = string[j], string[i]
            wordPermutations(string, i + 1, length)
            string[i], string[j] = string[j], string[i]


s = input()
x = int(input())
wordPermutations(list(s), 0, len(s))
l.sort()
for word in l:
    if word[x] == s[0]:
        print(word)
