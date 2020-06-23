# all the tests for user model go here.
import unittest
import jwt
import os
import json
from app import create_app
from app.api.models.db import db_init

KEY = os.getenv('SECRET_KEY')

class TestLists(unittest.TestCase):
    def setUp(self):
        """Set up tests"""
        
        self.app = create_app("testing")
        self.client = self.app.test_client() 
        db_init()
        self.test_user = {"firstname":"kabaki",\
            "email":"kabaki.kiarie@gmail.com","password":"Baniut490t4"}
        self.test_blank_username = {"firstname":"",\
            "email":"najuake@gmail.com","password":"Baniut490t4"}
        self.login_user = {"email":"kabaki.kiarie@gmail.com",
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
        response = self.client.post('/auth/signup'
        ,data=json.dumps(self.test_user), content_type='application/json')
        return response

    def test_user_creating_account_successfully(self):
        """Test the creation of an account"""
        response = self.post()
        self.assertEqual(response.status_code,201)
    
    def test_successful_user_login(self):
        """Test login """
        token = jwt.encode(
            {"email": "kabaki.kiarie@gmail.com"}, KEY, algorithm='HS256')
        self.post()
        self.client.get(f"/auth/verify?in={token.decode('utf-8')}")
        response = self.client.post(
            "/auth/signin", data=json.dumps({
                "email": "kabaki.kiarie@gmail.com",
                "password": "Baniut490t4"
            }),content_type="application/json")
        self.assertEqual(response.status_code, 200)     
    
    def test_user_creating_account_with_blank_field(self):
        """Test creating a user with a blank field"""
        self.post()
        response = self.client.post("/auth/signup"
        ,data=json.dumps(self.test_blank_username),content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_getting_all_users(self):
        """Test getting all users"""
        self.post()
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_getting_user_by_id(self):
        """Test getting a user by id"""
        self.post()
        response = self.client.get('/users/{}'.format(1))
        self.assertEqual(response.status_code,200)

    def test_signin_with_wrong_password(self):
        """Test sign in with a wrong password"""
        self.post()
        response = self.client.post(
            "/auth/signin", data=json.dumps({
                "email": "kabaki.kiarie@gmail.com",
                "password": "Baniut490t5"
            }),content_type="application/json")
        self.assertEqual(response.status_code, 401)
    
    def test_signup_already_existing_email(self):
        """Test signing up an already existing email"""
        self.post()
        response = self.post()
        self.assertEqual(response.status_code, 409)       

    def test_signup_with_missing_info(self):
        """Test sign up with some user info missing."""
        response = self.client.post('/auth/signup'
        ,data=json.dumps({"firstname":"kaba"})
        ,content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_signup_with_missing_password(self):
        """Test sign up with missing password"""
        response = self.client.post('/auth/signup'
        ,data=json.dumps({"firstname":"kaba",
        "email":"kaba@gmail.com"})
        ,content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_signin_with_a_non_existent_account(self):
        """Test sign in with a non exisistent account"""
        self.post()
        response = self.client.post(
            "/auth/signin", data=json.dumps({
                "email": "jkabak.kiarie@gmail.com",
                "password": "Baniut490t5"
            }),content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_signup_password_without_a_number(self):
        """Test sign up with a password without a number"""
        response = self.client.post('/auth/signup',
        data=json.dumps({"firstname":"kaba",
        "email":"kaba@gmail.com",
        "password":"Baniutxxca"}),content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_signup_password_without_caps(self):
        """Test sign up with a password without caps"""
        response = self.client.post('/auth/signup',
        data=json.dumps({"firstname":"kaba",
        "email":"kaba@gmail.com",
        "password":"aniutxxc23a"}),content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_signup_password_too_short(self):
        """Test sign up with a short password"""
        response = self.client.post('/auth/signup',
        data=json.dumps({"firstname":"kaba",
        "email":"kaba@gmail.com",
        "password":"Ba5ge"}),content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_signup_password_all_caps(self):
        """Test sign up with a password all caps"""
        response = self.client.post('/auth/signup',
        data=json.dumps({"firstname":"kabaf",
        "email":"mkaba@gmail.com",
        "password":"NADKJROR23"}),content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_update_user_password(self):
        """Test updating an existing user password"""
        self.post()
        response = self.client.post('/auth/newpass',
        data=json.dumps({"email":"kabaki.kiarie@gmail.com",
        "password":"Baniut490t6"}),content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_update_non_user_password(self):
        """Test updating an non existing user password"""
        self.post()
        response = self.client.post('/auth/newpass',
        data=json.dumps({"email":"gkabak.kiarie@gmail.com",
        "password":"Baniut490t6"}),content_type='application/json')
        self.assertEqual(response.status_code, 404)
    
    def test_update_a_password_missing_password(self):
        """Test updating a password with missing password"""
        self.post()
        response = self.client.post('/auth/newpass',
        data=json.dumps({"email":"kabaki.kiarie@gmail.com",
        "password":""}),content_type='application/json')
        self.assertEqual(response.status_code, 400)

        
    



        

