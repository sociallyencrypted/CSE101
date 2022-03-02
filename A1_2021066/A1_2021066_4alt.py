def satisfiable(fn):
    sat = False
    for b1 in [True, False]:
        for b2 in [True, False]:
            for b3 in [True, False]:
                if eval(fn):
                    sat = True
                    print(b1, b2, b3)
    return sat


cond = input("Enter a condition in b1, b2 and b3: ")
print (satisfiable(cond))
