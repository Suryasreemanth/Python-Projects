print("Welcome to play my Quiz game")

print("Do you want to play the game?")
play=input("Enter Yes/No: ")

if play.lower()=='no':
    quit()

else:
    print(" Answer the following questions")


score=0
ans=input("What does CPU stands for? ")
if ans.lower()=="central processing unit":
    score=score+1
    print("Correct!")
else:
    print("Incorrect!")

ans=int(input("How many iterators are present in Python? "))
if ans==2:
    score=score+1
    print("Correct!")
else:
    print("Incorrect!")

ans=input("Tag to print a horizontal line in HTML? ")
if ans.lower()=="<hr>":
    score=score+1
    print("Correct!")
else:
    print("Incorrect!")

ans=input("Tag to print a new line in HTML? ")
if ans.lower()=="<br>":
    score=score+1
    print("Correct!")
else:
    print("Incorrect!")

ans=input("Do lists are immutable? ")
if ans.lower()=="no":
    score=score+1
    print("Correct!")
else:
    print("Incorrect!")

if score==5:
    print("Hooray! You have answered all the questions correctly")

else:
    print("You have answered " + str(score)+" questions correctly")