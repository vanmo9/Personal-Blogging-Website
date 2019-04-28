import unittest
from app.models import User


class UserModelTest(unittest.TestCase):


    def setUp(self):
        self.new_user = User(password = 'moha' )
        
    # testcase test_password_setter this ascertains that when password is being hashed and the pass_secure contains a value.    
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)



    # taste case confirms that our application raises an AttributeError when we try and access the password property
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password


    # test confirms that our password_hash can be verified when we pass in the correct password.
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('moha'))