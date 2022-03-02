# (b1 and not b1)
sat = False
for b1 in [True, False]:
    if sat:
        break
    for b2 in [True, False]:
        if sat:
            break
        for b3 in [True, False]:
            if b1 and not b1:
                sat = True
                print("Satisfiable")
                print(b1, b2, b3)
                break
if not sat:
    print("Unsatisfiable")


# (b1 or b2) and (b2 or not b3)
sat = False
for b1 in [True, False]:
    if sat:
        break
    for b2 in [True, False]:
        if sat:
            break
        for b3 in [True, False]:
            if (b1 or b2) and (b2 or not b3):
                sat = True
                print("Satisfiable")
                print(b1, b2, b3)
                break
if not sat:
    print("Unsatisfiable")
sat = False
