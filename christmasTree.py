a = int(input("Enter height of tree branches"))
b = int(input("Enter height of tree stalk"))
for i in range(a):
    print(' '*(a-i),end='')
    print('*'*(2*(i+1)-1),end='')
    print(' '*(a-i))
for i in range(b):
    print(' '*(a-1),end='')
    print('*'*3,end='')
    print(' '*(a-1))