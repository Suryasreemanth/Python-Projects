import random

upper_range=input("Enter the upper range: ")

if upper_range.isdigit()==True:
    upper_range=int(upper_range)

else:
    print("please enter a positive integer")
    quit()

number=random.randint(1,upper_range)

while True:
    user_num=input("Type a number to guess: ")

    if user_num.isdigit()==True:
        user_num=int(user_num)
    else:
         print("please enter a positive integer next time")
         continue
   
    if user_num==number:
        print(" Hooray! You have guessed it correct!")
        break

    elif user_num>upper_range:
        print("You have entered a higher number than range")

    elif user_num<1:
        print("YOu have entered a integer less than 1")

    else:
        print("You got it wrong")