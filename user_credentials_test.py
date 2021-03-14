from user import User
import unittest # Importing the unittest module

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("diella","diella26") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"diella")
        self.assertEqual(self.new_user.password,"diella26")

    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.users_list),1)

    def test_save_multiple_user(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user.save_user()
            test_user = User("diella","diella26") # new contact
            test_user.save_user()
            self.assertEqual(len(User.users_list),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.users_list = []

# other test cases here
    def test_save_multiple_user(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_user.save_user()
        test_user = User("diella","diella26") # new contact
        test_user.save_user()
        self.assertEqual(len(User.users_list),2)

    def test_delete_user(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_user.save_user()
        test_user = User("diella","diella26") # new contact
        test_user.save_user()

        self.new_user.delete_user()# Deleting a contact object
        self.assertEqual(len(User.users_list),1)

    def test_find_user_by_user_name(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("diella","diella26") # new contact
        test_user.save_user()

        found_user = User.find_user_by_user_name("diella26")

        self.assertEqual(found_user.user_name,test_user.user_name) 

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("diella","diella26") # new contact
        test_user.save_user()

        user_exists = User.user_exist("diella")

        self.assertTrue(user_exists)    

    def test_display_all_user(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(User.display_user(),User.users_list)


if __name__ == '__main__':
    unittest.main()