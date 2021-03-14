#!/usr/bin/env python3.6

from user import User
from accounts import Credentials
import random
import string
import pickle
import time


def create_account(fullname, username, password):
    """
    Function for creating a new user account
    """

    new_user = User(fullname, username, password)
    return new_user


def save_user(user):
    '''
    Function to save new user credentials
    '''
    User.save_user(user)


def verify_user_login(user_name, user_password):
    """
    funtion to verify user input and log in accout details
    """

    account_exist = User.verify_user(user_name, user_password)
    # print("verify_user_login")
    # print(account_exist)
    return account_exist


def create_new_credentials(acc_name, acc_username, acc_password):
    """
    Funtion for creating new user credentials
    """
    new_user_credentials = Credentials(acc_name, acc_username, acc_password)
    return new_user_credentials


def save_new_user_credentials(credential):
    """
    funtion to save user credentials
    """

    credential.save_existing_acc()


def del_user_credentials(credential):
    """
    funtion to delete user credentials
    """
    print('wos')
    return credential.delete_user_credentials()


def dis_user_credentials():
    """
    funtion that returns all saved contacts
    """

    return Credentials.display_user_credentials()


def generate_password():
    """Funtion that generates random password for the user"""

    gen_password = Credentials.generate_password()
    return gen_password


def find_account(username):
    """
    a method funtion for the user to search for a specific account using its username.
    """
    return Credentials.find_by_username(username)


def check_existing_accounts(username):
    """
    Function that checks if an account exists and returns a boolean value
    """
    return Credentials.account_exists(username)


def main():
    command = ''
    print('*'*80)
    print('Welcome to Password Locker!\n')
    print('*'*80)
    while True:
        time.sleep(1)
        print("""
        Use the following commands to procceed:
        New - New user
        Log - Log into account
        Quit - Terminate process
      """)
        command = input(
            'Please choose a command to continue : ').lower().strip()
        print('\nProcessing...')
        time.sleep(1.5)

        if command == 'new':
            print('\n')
            print('*'*80)
            fullname = input('Enter full name : ')
            user_name = input('Enter username : ')
            password = input('Enter password : ')
            confirm_password = input("Confirm password : ")
            print('\nCreating Account...')
            time.sleep(0.5)
            print('\n')

            while password != confirm_password:
                print('Checking password...\n')
                time.sleep(1)
                print("Sorry. Password didn't not match. Please try again... \n")
                confirm_password = input('Confirm password : ')
                print('\n')
            else:
                print('\nCreating account...\n')
                time.sleep(1)
                print('*'*80)
                print(
                    f'Welcome {user_name}. Your account has been created succesfully!')
                print('*'*80)
                print(
                    "Proceed to Login to your account. Use the command 'log' to login. \n")
                print('*'*80)
            save_user(create_account(
                fullname, user_name, password))

        elif command == 'log':
            time.sleep(0.5)
            username_input = input('Username : ')
            password_input = input('Password : ')
            print('\nLogging in...\n')
            time.sleep(1)
            log_in = verify_user_login(username_input, password_input)

            if log_in == False:
                print('Checking account...\n')
                time.sleep(1)
                print('*'*80)
                print(
                    "Sorry. The account doesn't exist. Please try again or create an account to access Password Locker\n")
                print('*'*80)
                print('\n')

            else:
                time.sleep(0.5)
                print('*'*80)
                print('Login Successful! \n')
                time.sleep(0.5)
                print(
                    f'Your user name is {username_input} and password {password_input} \n')
                print('*'*80)

                while True:
                    time.sleep(1)
                    print(
                        'Proceed to manage your account. Use the following short-codes to navigate through the application :')
                    print("""
          nw - create new account credentials
          vw - view existing credentials
          sr - search for an account
          dl - delete account credentials
          ex - exit
          \n
                      """)
                    time.sleep(0.5)
                    short_code_choice = input(
                        'Please choose a command : ').lower().strip()
                    if short_code_choice == 'nw':
                        print('Fill in the account details you want to store..')
                        account_name = input('Account name : ')
                        account_username = input('Account username : ')
                        print('\nProcessing...\n')

                        while True:
                            print("""
        Would you like to use your own password or a random generated password?
        Use short-codes:
            my - your password choice
            gp - to generate password
        """)
                            user_choice = input("> ").lower().strip()
                            if user_choice == 'my':
                                user_choice_pass = input('Your password :')
                                break
                            elif user_choice == 'gp':
                                user_choice_pass = generate_password()
                                break
                            else:
                                print('\nProcessing...\n')
                                time.sleep(1)
                                print(
                                    "Sorry. I didn't catch that. Try again please...")

                        save_new_user_credentials(create_new_credentials(
                            account_name, account_username, user_choice_pass))
                        time.sleep(1)
                        print('*'*80)
                        print(
                            f'User Account :\n Page-name : {account_name}\n Username : {account_username}\n Password : {user_choice_pass}')
                        print('*'*80)
                        print("\n")

                    elif short_code_choice == 'vw':
                        if dis_user_credentials():
                            print('Here is a list of your current credentials : ')
                            time.sleep(1)
                            print('*'*80)
                            for credential in dis_user_credentials():
                                print(
                                    f'Account name : {credential.acc_name}\nUsername : {credential.acc_username}\nPassword : {credential.acc_password}')
                                print('*'*80)
                                print("\n")
                        else:
                            print('\nProcessing...\n')
                            time.sleep(1)
                            print('*'*80)
                            print(
                                "Sorry. You don't seem to have any acounts yet. Would you like to create an account?")
                            print('*'*80)
                            print("\n")

                    elif short_code_choice == 'sr':
                        print('Enter the username you want to search for : ')
                        time.sleep(0.5)
                        search_term = input('> ')
                        print('\n')
                        print('*'*80)
                        if check_existing_accounts(search_term):
                            search_account = find_account(search_term)
                            print('\nLoading accounts...\n')
                            time.sleep(1)
                            print(
                                f'The account was found :\nAccount name : {search_account.acc_name}\nAccount username : {search_account.acc_username}\nPassword : {search_account.acc_password}')
                            print('*'*80)

                        else:
                            print('\nProcessing...\n')
                            time.sleep(1)
                            print('*'*80)
                            print('The account you are looking for does not exist.')
                            print('*'*80)
                            print('\n')

                    elif short_code_choice == 'dl':
                        print("Enter the account username you want to delete")
                        search_input = input('>').lower()
                        if find_account(search_input):
                            account_search = find_account(search_input)
                            print("\n")
                            account_search.delete_user_credentials()
                            print('\nDeleting...\n')
                            time.sleep(1)
                            print(f"Your account was successfully deleted!")
                            print('*'*80)
                        else:
                            print('\nProcessing...\n')
                            time.sleep(1.5)
                            print('*'*80)
                            print(
                                "Sorry. The account you are looking for does not exist\n")
                            print('*'*80)
                            print('\n')

                    elif short_code_choice == 'ex':
                        print('\nExiting...\n')
                        time.sleep(1)
                        print("Thank you!\n")
                        break

                    else:
                        print('\nProcessing...\n')
                        time.sleep(1)
                        print('Sorry. I didnt catch that. Try again..\n')

        elif command == 'quit':
            time.sleep(0.5)
            print('*'*80)
            print("Thank you for using Password Locker. See you soon!")
            print('*'*80)
            print('\n')
            break
        else:
            print('*'*80)
            print(
                "Sorry I didn't understand that command. Please enter a valid command.")
            print('*'*80)
            print('\n')


if __name__ == '__main__':
    main()
