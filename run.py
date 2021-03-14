#!/usr/bin/env python3.6
from user_credentials_test import User

def create_username(u_name, p_password):
	'''
	Function to create a new user account
	'''
	new_user = User(u_name,p_password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)

def display_user():
	'''
	Function to display user saved by a user
	'''
	return User.display_user()

def delete_user(user):
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        return User.delete_users(user)

def find_user(user):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_user_by_user_name(user)       
     
def check_existing_users(user):
    '''
    Function that check if a user exists 
    '''
    return User.user_exist(user)



def main():
    print("Hello Welcome to your user list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cu - create a new username, du - display username, dl - delete user, fu -find a username, ex -exit the users list ")

                    short_code = input().lower()

                    if short_code == 'cu':

                            print ("User name ....")
                            u_name= input()

                            print("Password ...")
                            password= input()

                            save_user(create_username(u_name,password)) # create and save new contact.
                            print ('\n')
                            print(f"New user {u_name} {password} created")
                            print ('\n')

                    elif short_code == 'du':

                            if display_user():
                                    print("Here is a list of all your username")
                                    print('\n')

                                    for user in display_user():
                                            print(f"{user.user_name}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any user saved yet")
                                    print('\n')

                    elif short_code == 'fu':

                            print("Enter the username you want to search for")

                            search_user = input()
                            if check_existing_users(search_user):
                                    search_user = find_user(search_user)
                                    print(f"{search_user.user_name} {search_user.password}")
                                    print('-' * 20)
                            else:
                                    print("That user does not exist")

                    
                            
                 
                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()