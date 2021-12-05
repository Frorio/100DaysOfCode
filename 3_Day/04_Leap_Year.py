year = int(input("Input any year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leak year!")
        else: print("Not leak")
    else: print("Not leak")
else: print("Not leak")