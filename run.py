
import string
from random import *
from user import User
from user import Credentials

def create_user(username,userpassword):
    newuser= User(username,userpassword)
    return newuser
def save_user(User):
    User.save_user()
def find_user(number):
    return User.find_by_number(number)
def create_account(accountusername,accountname,accountpassword):
    newaccount= Credentials(accountusername,accountname,accountpassword)
    return newaccount 
def save_account(User):
    User.save_account()
def delete_account(Credentials):
    Credentials.delete_account()
def find_account(number):
    return Credentials.find_by_number(number)
def display_accounts():
    return Credentials.display_accounts()

def main():
        
            print("Welcome to Password Locker! Created By Joylene Kirui.")
            print("-----------------------------------------------------")
            print("1. Sign Up \n 2. Login")
            while True:
                option=input("Select to Continue \n")
                if option in ['1', '2']:
                    break
                else :
                    print("kindly input a valid option")
                    print(" 1.Sign Up \n 2.Login")
            if option == "1":
                signUp()
            else :
                logIn()
              
def signUp() :
    print("Create Account")
    while True :
        print("-"*10)
        print("Set your username..")
        username=input()
        print("Set your password..")
        userpassword=input()
        save_user(create_user(username,userpassword))
        print(f"\n Great {username}, Your account was created successfully.These are your Account details:")
        print("-"*10)
        print(f"Username: {username} \nPassword: {userpassword}")
        print("\nYou can now Login to your account")
        print("\n \n")
        logIn()
    
    
def logIn() :
        print("LOGIN")
        print("Enter Username..")
        loginUsername=input()
        print("Enter Password..")
        loginPassword=input()
        if find_user(loginPassword):
            print("Select to Continue\n 1. Add account credentials \n 2. View Accounts \n 3. Delete Account \n 4.Log Off")
            print("-"*60)
            choose= input()
            print("\n")
            if choose == "1":
                print("Enter Your Account credentials")
                print("-"*25)
                accountusername=loginUsername
                print("Account Name")
                accountname=input()
                print("\n")
                print("Select to create password\n 1. Generate automatic password \n 2. Create new password")
                decision=input()
                if decision =="1":
                    characters=string.ascii_letters + string.digits
                    accountpassword="".join(choice(characters)for x in range(randint(6,16)))
                    print(f"Password: {accountpassword}")
                    save_account(create_account(accountusername,accountname,accountpassword))
                   
                elif decision =="2":
                    print("Enter your Password(upto 4 characters)")
                    accountpassword=input()
                    save_account(create_account(accountusername,accountname,accountpassword))
                else:
                    print("please put in a valid choice")  
                    logIn()
                
                print("\n")
                print(f"Username:{accountusername} \nAccount Name: {accountname} \nPassword: {accountpassword}") 
            elif choose == "2":
                if find_account(loginUsername):
                    print("Here is a list of your created accounts: ")
                    print("-"*25)
                    for user in display_accounts():
                        print(f"Account: {user.accountname} \nPassword: {user.accountpassword} \n\n")
                else:
                    print("Invalid creds | You have no account credentials yet!") 
                    logIn()    
                
            elif choose == "3":
                print("Confirm username")
                accountusername = input()
                print("Enter the account name of the Credentials you want to delete")
                accountname = input()
                print("Enter the password of the account Credentials you want to delete")
                accountpassword = input()
                
                if find_account(accountpassword):    
                    Credentials.delete_account
                    print('\n')
                    print(f"You  have deleted your account credentials successfully!!")
                    print('\n')
                else:
                    print(f"The {accountname} credentials You want to delete does not Exist in this locker!!")
                    logIn()
            elif choose == "4":
                print("You are logged off, thank you for using Password Locker!\n")
                main()
            else :
                print("invalid option! Try Again \n")
                
                logIn()

        else:
            print("Incorrect INFO please try again! Thankyou")
            print("\n")
            main()
            
            
if __name__ == '__main__':
     main()