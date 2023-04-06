while 1:    
    num = input("Please Enter a Number: ")
    num2 = int(num)
    if not num.isnumeric():
        print("Invald Input, Please try again.")
    if num2 < 10:
    	print("Koochice!")
    elif 10 <= num2 < 100:
    	print("Bozorge!")
    elif 100 <= num2 < 1000:
    	print("Kheili Bozorge!")
    else:
    	print("Idon't know what to say dude :)")
    
    answer = input("Try Again? Y/n ")
    while 1:
        if answer.isnumeric() or ((answer != "Y" and answer != "y") and (answer != "n" and answer != "N")):
            print("Invalid Input, Please try again.")
            answer = input("Try Again? Y/n ")
            continue
        else:
            break
    if answer == "Y" or answer == "y":
        continue
    else:
        break
