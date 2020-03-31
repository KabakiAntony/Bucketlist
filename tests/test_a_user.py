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
        self.test_blank_username = {"firstname":"",\
            "email":"akabak.kiarie@gmail.com","password":"Baniut490t4"}
        self.login_user = {"email":"kabak.kiarie@gmail.com",
            "password":"Baniut490t4"}

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
    
    def test_successful_user_login(self):
        """Test user login """
        self.post()
        response = self.client.post('/bucket/signin'
        ,data=json.dumps({"email":"kabak.kiarie@gmail.com",
        "password":"Baniut490t4"}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_user_creating_account_with_blank_field(self):
        """Test creating a user with a blank field"""
        self.post()
        response = self.client.post("/bucket/signup"
        ,data=json.dumps(self.test_blank_username),content_type="application/json")
        self.assertEqual(response.status_code, 400)
        
    
    