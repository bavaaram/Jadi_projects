import random
guess = list()
i = 0
num = input("Please Enter your integer number between 0 & 100: ")
print("You can navigate with b = Bozorgtar, m = Mosavi, k = Koochiktar.")
a, b = 0, 100
guess.append(random.randint(a, b))
print("My guessed number is %s" % str(guess[i]))
flag = input("Please navigate your number situation: b/m/k ")

while num != guess:
    if flag == "b":
        a = guess[i]
        guess.append(random.randint(a, b))
        print("My guessed number is %s" % str(guess[i + 1]))
        i += 1
        flag = input("Please navigate your number situation: b/m/k ")
        continue

    if flag == "k":
        b = guess[i]
        guess.append(random.randint(a, b))
        print("My guessed number is %s" % str(guess[i + 1]))
        i += 1
        flag = input("Please navigate your number situation: b/m/k ")
        continue

    if flag == "m":
        print("The system won! ")
        break

print("The list of guessed numbers by system:\n")
print(guess)
