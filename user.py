class User:
    """
    User class for creating password locker account and logging in
    """
    user_credentials = []

    def __init__(self, fullname, username, password):
        self.fullname = fullname
        self.username = username
        self.password = password

    def save_user(self):
        """
        a funtion for saving user credentials after creating a account
        """

        User.user_credentials.append(self)

    @classmethod
    def verify_user(cls, user_name, user_password):
        """
        verify is the user has created an account and exists in the list.Returns a boolean value
        """
        if len(cls.user_credentials) == 0:
            return False
        else:
            for user in cls.user_credentials:
                if user.username == user_name and user.password == user_password:
                    return True
                return False
