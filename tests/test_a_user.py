# all the tests for user model go here.
import unittest
import json
from app import create_app
from app.api.models.db import db_init

class TestLists(unittest.TestCase):
    def setUp(self):
        """Set up tests"""
        
        self.app = create_app("testing")
        self.client = self.app.test_client() 
        db_init()
        self.test_user = {"firstname":"kabaki",\
            "email":"kabak.kiarie@gmail.com","password":"Baniut490t4"}

    # there will be no teardown in this test module 
    # since I want the database to clear after all tests
    # have run.
    
    def post(self,data={}):
        """ This is just a helper method for the 
        test cases that need to post data see
        comments for more explanation."""
        if not data:
            data = self.test_user
        response = self.client.post('/bucket/signup'
        ,data=json.dumps(self.test_user), content_type='application/json')
        return response

    def test_user_creating_account_successfully(self):
        """Test the creation of an account"""
        response = self.post()
        self.assertEqual(response.status_code,201)
    
    