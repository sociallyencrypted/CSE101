try:
    RA_factor, Age = [int(i) for i in input().split()]
    RA_score = 1 / (RA_factor - Age)
    print(f"{RA_score:.2f}")
except:
    print("Ambivert")
