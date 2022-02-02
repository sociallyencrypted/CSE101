def hasDigit(s):
    for i in list(s):
        if i.isdigit():
            return True
    return False

def hasAlpha(s):
    for i in list(s):
        if i.lower().isalpha():
            return True
    return False

n = int(input())
l = []
count = 0
for i in range(n):
    x = input()
    if  x.count('@') == 1 and x.count('.') == 1 and x.find('@') < x.find('.') and hasDigit(x) and hasAlpha(x) and not hasDigit(x[x.find('@')+1:]) and x.replace('@','').replace('.','').isalnum():
        l.append(x)
        
print(len(l))
for j in range(len(l)):
    print(l[j])