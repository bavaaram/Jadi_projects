import random

while 1:
    print("Welcome to number guessing game.")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    flag = input(("ready for start? Y/n "))
    charge = 10

    while 1:
        if (flag == "Y" or flag == "y") or (flag == "N") or (flag == "n"):
            break
        else:
            print("Invalid Input, please try again.")
            flag = input(("ready for start? Y/n "))
            continue

    if (flag == "N") or (flag == "n"):
        print("Exiting the program...")
        break

    num = random.randint(0, 100)
    print("The number is generated.")
    print("Remember, you have 10 chances to guess :)")
    print("************************************************************\n")
    print("%s Guesses remaining" % charge)
    guess = int(input("Enter your guess: "))

    while 1:
        if charge == 1:
            if num != guess:
                print("You Lost! ")
                print("The number is %s" % str(num))
                break

        if (guess > num) and charge > 1:
            charge -= 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("The guessed number in greater.")
            print("%s Guesses remaining" % charge)
            guess = int(input("Enter your guess: "))
            continue

        if (guess < num) and charge > 1:
            charge -= 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("The guessed number in smaller.")
            print("%s Guesses remaining" % charge)
            guess = int(input("Enter your guess: "))
            continue

        if num == guess:
            print("Congrats, you win! ")
            break


    break

