
userChoice = int(input("Enter number of day of week from 1 to 7:"))

if userChoice >= 1 and userChoice <=7:
    if userChoice == 1:
        print("In England this is Sunday")
    elif userChoice == 2:
        print("In England this is Monday")
    elif userChoice == 3:
        print("In England this is Tuesday")
    elif userChoice == 4:
        print("In England this is Wednesday")
    elif userChoice == 5:
        print("In England this is Thursday")
    elif userChoice == 6:
        print("In England this is Friday")
    elif userChoice == 7:
        print("In England this is Saturday")
else:
    print("Week has only 7 days")
