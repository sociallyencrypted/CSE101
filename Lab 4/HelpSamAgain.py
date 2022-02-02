def findMaxLength(string):
    lptr=0
    rptr=1
    count=0
    maxc=0
    while(rptr<=len(string)):
        if len(set(string[lptr:rptr]))<=2:
            rptr+=1
            count+=1
            maxc=max(count,maxc)
        else:
            lptr+=1
            rptr=lptr+1
            count=0
            
    return maxc

x = input()
print(findMaxLength(x))
        