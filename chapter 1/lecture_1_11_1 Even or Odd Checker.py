num = input("Please Enter a number: ")
while 1:
    if not num.isnumeric():
        print("Invalid input, Please try again. ")
        num = input("Please Enter a number: ")
        continue
    else:
        break
    
num2 = int(num)
if num2 % 2 == 0:
    print("Is Even! ")
else:
    print("is Odd! ")
    
