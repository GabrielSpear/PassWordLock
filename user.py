import random
from credentials import Credentials

def create_credentials(fname,lname,phone,email):
    '''
    Create new User
    '''
    new_user = Credentials(fname,lname,phone,email)
    return new_user

def save_credentials(credentials):
    '''
    saves credentials
    '''
    credentials.save_credentials()

def display_credentials():
    '''
    displays user Credentials
    '''
    return Credentials.display_credentials()

def main():
    print("We will help you save all your credentials and generate passwords for you as well.")

    user_name = input()

    print(f"Hello {user_name}. What brought you here?")
    print('\n')

    while True:
        print("Use the following to navigate through the app: new - create new account,display - display contacts,pg - password generation,exit - if you wanna leave")
        initials = input().lower()

        if initials =='new':
            print("Sign up")
            print("-"*10)

            print("Input your first name")
            f_name = input()

            print("Input your last name")
            l_name = input()

            print("Input your mobile phone number")
            p_number = input()

            print("Input your email address")
            e_address = input()

            save_credentials(create_credentials(f_name,l_name,p_number,e_address))

            print ('\n')
            print(f"New Account {f_name}{l_name} is saved")


        elif initials == 'display':

            if display_credentials():
                print("These are your currently saved credentials.")
                print('\n')
                for credentials in display_credentials():
                    print(f"{credentials.first_name} {credentials.last_name}...{credentials.number}")
                    print('\n')
                else:
                    print('\n')
                    print("No Other Accounts")
                    print ('\n')

        elif initials == 'pg':

                choices = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ?()@#$%^&*!"
                length = len(choices)
                print("Provide the minimum length requires for your password")
                lent = int(input())
                password = "".join(random.sample(choices,lent ))
                print ('\n')

                print(password)

        elif initials == 'exit':

                print("Thank you, Waiting to see you again")
                break

        else:
                print("Please use required inputs")

if __name__ == '__main__':
    main()
