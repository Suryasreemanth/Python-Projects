mater_pwd=input("What is the master password ? ")

def view():
    
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            
            user,pwd=data.split()
            print("User is",user,"and ","Password is ",pwd)

def add():

    account_name=input("Enter name of the account: ")
    pwd=input("Enter password: ")

    with open('password.txt','a') as f:
        f.write(account_name +"  "+ pwd+"\n")

while True:
    mode=input(' Would you like to view the current password or add an new password (view/add) or press q to quit? ').lower()

    if mode=='q':
        print(" You have ended it")
        break

    elif mode=='view':
        view()

    elif mode=='add':
        add()

        