import unittest
from user import user

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
def test_delete_user(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_contact.save_contact()
            test_user = user("Joy","1234",) 
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(user.user_list),1)              




if __name__ == '__main__':
    unittest.main()   