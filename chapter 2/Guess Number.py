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

    def num_check(a):       #A function for number healthly check and avoid to pass string characters & out of range numbers.
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
    guess = 0
    print("The number is generated.")
    print("************************************************************\n")
    print("%s Guesses remaining" % charge)
    guess = num_check(guess)        #check the guess for its healthly before enter to the conditions via num_check function.

    while int(guess) != num:        #Until the guess and the number not equal to each other, this while loop will run. if num & guess are equal, we will beark this while loop.
        if charge == 1:     #If chance was reached 1 and eventually mistake in guessing, the player chances ran out and he/she lose the game.
            if num != int(guess):
                print("You Lost! ")
                print("The number is %s" % str(num))
                break

        if (int(guess) > num) and charge > 1:       #A condition for greater mode.
            charge -= 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("The guessed number in greater.")
            print("%s Guesses remaining" % charge)
            guess = num_check(guess)
            continue

        if (int(guess) < num) and charge > 1:       #A condition for smaller mode.
            charge -= 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("The guessed number in smaller.")
            print("%s Guesses remaining" % charge)
            guess = num_check(guess)
            continue
    print("Congrats, you win! ")        #A condition for correct guessing mode (winning in the game).

    print("\n*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n") 
    ans = input("Play again? Y/n ")
    while 1:        #A loop for check "ans" input healthly to avoid pass characters instead of Y, y and N, n through the conditional statements.
        if ans == "Y" or ans == "y" or ans == "N" or ans == "n":        #If ans equal to Y or y or N or n, pass it through the healthly check.
            break
        else:       #Everything entered for "ans" instead of 4 characters listed previous comment will be denied and player must enter the "ans" again.
            print("Invalid Input, please try again.")
            ans = input(("ready for start? Y/n "))
            continue

    if ans == "Y" or ans == "y":        #If player enter Y or y, pass him/her through the base loop (first line while 1:) ans continue.
        print("Restarting the program...")
        print("\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
        continue
    elif ans == "N" or ans == "n":      #If player enter N or n, exiting the whole program and break the base loop (first line while 1:).
        print("Exiting the program...")
        break
