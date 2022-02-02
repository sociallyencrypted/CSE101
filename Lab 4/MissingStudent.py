l = [int(element) for element in input().split()]
for i in l:
    if i % 2 == 0:
        print('1',end='')
    else:
        print('0',end='')