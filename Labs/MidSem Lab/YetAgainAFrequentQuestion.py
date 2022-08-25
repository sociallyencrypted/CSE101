count = {}


def buildDict(s):
    for x in s.strip().split(" "):
        if len(x) > 1:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1


string = input()
buildDict(string)
x = list(count.keys())
x.sort()
for key in x:
    print(key, ":", count[key])
