from random import *
import string


class Credentials:
    """
    a class for user accounts and account details
    """
    user_credential_list = []

    def __init__(self, acc_name, acc_username, acc_password):
        self.acc_name = acc_name
        self.acc_username = acc_username
        self.acc_password = acc_password

    def save_existing_acc(self):
        """
        function to save existing user credentials
        """
        Credentials.user_credential_list.append(self)

    @classmethod
    def display_user_credentials(cls):
        """
        funtion to display existing user credentials
        """
        return cls.user_credential_list

    @classmethod
    def generate_password(cls):
        '''
        Method that generates a random password
        '''
        charcaters = string.ascii_uppercase+string.ascii_lowercase+string.digits
        password = ''.join(choice(charcaters) for x in range(randint(8, 16)))

        return password

    @classmethod
    def account_exists(cls, username):
        """
        Method that checks if a username exists in an account.
        Searches using a username and returns a boolean value
        """
        for name in cls.user_credential_list:
            if name.acc_username == username:
                return True
        return False

    @classmethod
    def find_by_username(cls, username):
        """
        Method that takes in a username and returns an account that matches that ussername
        """
        for name in cls.user_credential_list:
            if name.acc_username == username:
                return name

    def delete_user_credentials(self):
        """
        deletes a saved user credential from the list
        """

        Credentials.user_credential_list.remove(self)
