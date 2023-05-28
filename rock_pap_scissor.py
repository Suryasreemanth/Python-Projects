import random

user_win=0
comp_win=0
tot_games=0
list=['Rock','paper',"Scissor"]

while True:
    tot_games=tot_games+1
    user_choice=input("Enter any of this (Rock/Paper/Scissor) and If you want to exit Type Q: ").lower()
    comp_choice=random.choice(list).lower()

    if user_choice not in ["rock",'paper',"scissor",'q']:
        print("You can only enter rock,paper, and scissor or quit the game by entering 'q' ")
        continue

    if user_choice=='rock' and comp_choice=='scissor':
        user_win=user_win+1
        print("You have won")

    elif user_choice=='scissor' and comp_choice=='paper':
        user_win=user_win+1
        print("You have won")

    elif user_choice=='paper' and comp_choice=='rock':
        user_win=user_win+1
        print("You have won")
    
    elif user_choice==comp_choice:
        print("It's a Tie!!")

    elif user_choice=='q':
        print("Game has ended")
        break

    else:
        comp_win=comp_win+1
        print("You have lost", comp_choice)

print("User has won", user_win, "times")
print("Computer have won", comp_win, "times")