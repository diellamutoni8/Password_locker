import unittest
from user import User


class TestUser(unittest.TestCase):
    """class that defines test cases for the user class"""

    def setUp(self):
        """
        defines instructions that would be executed before each test cases
        """
        self.new_user = User(
            'Diella Mutoni', 'diella', 'test123')

    def tearDown(self):
        """funtion that does clean up after each test case"""

        User.user_credentials = []

    # 1st test

    def test_init(self):
        """
        Test if the object has been initialized corretly
        """

        self.assertEqual(self.new_user.fullname, 'Diella Mutoni')
        self.assertEqual(self.new_user.username, 'diella')
        self.assertEqual(self.new_user.password, 'test123')

    # 2nd test if the user details are saved
    def test_save_user(self):
        """
        function to see if the new user credentials are being appended into the list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_credentials), 1)

    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_user.save_user()
        new_user_data = User("Diella Mutoni", "diella", "Mfh45hfk")
        new_user_data.save_user()
        user_data = User.verify_user('diella', "Mfh45hfk")
        self.assertFalse(user_data)


if __name__ == '__main__':
    unittest.main()
