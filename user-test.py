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
        self.new_user = user("Joy","1234") 
        
def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Joy")
        
       
        self.assertEqual(self.new_user.password,"1234")
def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(user.user_list),1)  


def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            user.user_list = []

def test_save_multiple_users(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_user.save_user()
        test_user = user("user","0712345678") # new contact
        test_user.save_user()
        self.assertEqual(len(user.user_list),2)


if __name__ == '__main__':
    unittest.main()   