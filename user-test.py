import unittest
from user import Credentials, User


class Testuser(unittest.TestCase):
        
        '''
        Test class that defines test cases for the user class behaviours.
        Args:
                unittest.TestCase: TestCase class that helps in creating test cases
        '''
        def setUp(self):
                '''
                Set up method to run before each test cases.
                '''
                self.new_user = User("Joy","1234") 
                self.new_account = Credentials("Joy","Insta","1234")
                        
        def test_init(self):
                '''
                test_init test case to test if the object is initialized properly
                '''

                self.assertEqual(self.new_user.username,"Joy")
                self.assertEqual(self.new_user.userpassword,"1234")

                self.assertEqual(self.new_account.accountusername,"Joy")
                self.assertEqual(self.new_account.accountname,"Insta") 
                self.assertEqual(self.new_account.accountpassword,"1234")

        def test_save_user(self):
                '''
                test_save_user test case to test if the user object is saved into
                the user list
                '''
                self.new_user.save_user() 
                self.assertEqual(len(User.userslist),1)  
        def test_save_account(self):
                '''
                test_save_user test case to test if the user object is saved into
                the user list
                '''
                self.new_account.save_account() 
                self.assertEqual(len(Credentials.accounts),1)  


        def tearDown(self):
                '''
                tearDown method that does clean up after each test case has run.
                '''
                User.userslist = []

        def test_save_multiple_users(self):
                '''
                test_save_multiple_users to check if we can save multiple contact
                objects to our contact_list
                '''
                self.new_user.save_user()
                test_user = User("user","0712345678") # new contact
                test_user.save_user()
                self.assertEqual(len(User.userslist),2)

        # def test_delete_account(self):
        #         '''
        #         test_delete_contact to test if we can remove a contact from our contact list
        #         '''
        #         self.new_account.delete_account()
        #         test_credentials = Credentials("Mark","Instagram","09876") # new contact
        #         test_credentials.save_account()

        #         self.new_account.delete_account()# Deleting account object
        #         self.assertEqual(len(Credentials.accounts),1)

        # def test_copy_password(self):
        #         '''
        #         Test to confirm that we are copying the password from a found account
        #         '''

        #         self.new_account.save_account()
        #         Credentials.copy_password("0712345678")

        #         self.assertEqual(self.new_account.accountpassword,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()    