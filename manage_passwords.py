mater_pwd=input("What is the password for master's ? ")

def view():
    
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            
            user,pwd=data.split()
            print("User : ",user,"and ","Password : ",pwd)

def add():

    account_name=input("Enter name of your account: ")
    pwd=input("Enter password: ")

    with open('password.txt','a') as f:
        f.write(account_name +"  "+ pwd+"\n")

while True:
    mode=input(' Would you like to view the current password or add an new password (view/add) or press q to quit? ').lower()

    if mode=='q':
        print(" You have ended the program")
        break

    elif mode=='view':
        view()

    elif mode=='add':
        add()

        