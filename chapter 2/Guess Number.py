import random

while 1:
    print("Welcome to number guessing game.")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
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

    def num_check(a):
        while 1:
            a = input("Enter your guess: ")
            if not a.isnumeric():
                print("Invalid Input, Please try again.")
                continue
            if 1 <= int(a) <= 100:
                break
            else:
                print("The entered number is out of range, please try again.")
                continue
        return a

    num = random.randint(0, 100)
    print("The generated number is %s" % str(num))
    guess = 0
    print("The number is generated.")
    print("Remember, you have 10 chances to guess :)")
    print("************************************************************\n")
    print("%s Guesses remaining" % charge)
    guess = num_check(guess)
    while 1:
        if charge == 1:
            if num != int(guess):
                print("You Lost! ")
                print("The number is %s" % str(num))
                break

        if (int(guess) > num) and charge > 1:
            charge -= 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("The guessed number in greater.")
            print("%s Guesses remaining" % charge)
            guess = num_check(guess)
            continue

        if (int(guess) < num) and charge > 1:
            charge -= 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("The guessed number in smaller.")
            print("%s Guesses remaining" % charge)
            guess = num_check(guess)
            continue

        if num == int(guess):
            print("Congrats, you win! ")
            break
    print("\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n") 
    ans = input("Play again? Y/n ")
    while 1:
        if ans == "Y" or ans == "y" or ans == "N" or ans == "n":
            break
        else:
            print("Invalid Input, please try again.")
            ans = input(("ready for start? Y/n "))
            continue

    if ans == "Y" or ans == "y":
        print("Restarting the program...")
        print("\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
        continue
    elif ans == "N" or ans == "n":
        print("Exiting the program...")
        break