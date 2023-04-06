while 1:    
    while 1:
        grade = input("Please Enter your Grade between 0 - 20: ")
        if not grade.isnumeric():
            print("Invalid Input, Please Try again.")
            continue
        else:
            break

        if not (0 <= int(grade) <= 20):
            print("The Entered Grade is out of Range, PLease try again.")
            continue
        else:
            break
    grade2 = float(grade)

    if 0 <= grade2 < 5:
        print("Your Grade is D+ ") if grade2 >= 2.5 else print("Your Grade is D ")
    if 5 <= grade2 < 10: 
        print("Your Grade is C+ ") if grade2 >= 7.5 else print("Your Grade is C ")
    if 10 <= grade2 < 15:
        print("Your Grade is B+ ") if grade2 >= 12.5 else print("Your Grade is B ")
    if 15 <= grade2 <= 20:
        print("Your Grade is A+ ") if grade2 >= 17.5 else print("Your Grade is A ")

