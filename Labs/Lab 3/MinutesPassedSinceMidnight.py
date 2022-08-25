def is_valid(hours, minutes):
    if hours <= 23 and minutes<=59:
        return("Valid")
    else:
        return("Invalid")


hours = int(input())
minutes = int(input())
if is_valid(hours, minutes) == "Valid":
    print(hours * 60 + minutes)
else:
    print("Invalid")