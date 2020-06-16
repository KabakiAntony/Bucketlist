# all the tests for lists go here.
# there will be no db_init() being called here
# since the database has already been initiated 
# in the first test module.

import unittest
import json
import jwt
import os
from app import create_app
from app.api.models.db import db_init

KEY = os.getenv('SECRET_KEY')

class TestLists(unittest.TestCase):
    def setUp(self):
        """Set up tests"""
        
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.test_list = {"content": "test list","user_id":1}
        self.updated_list = {"post_id":1,"content": "updating list","user_id":1}
        

    def tearDown(self):
        """Clear the db after tests finish running"""
        #db_init()
    
    def post(self,data={}):
        """ This is just a helper method for the 
        test cases that need to post data see
        comments for more explanation."""  
        user_token = jwt.encode(
            {"email": "kabaki.kiarie@gmail.com"}, KEY, algorithm='HS256')
        if not data:
            data = self.test_list
        response = self.client.post('/lists'
        ,data=json.dumps(self.test_list),
        headers={'x-access-token': user_token},
        content_type='application/json')
        return response
    
    def test_creating_validated_list(self):
        """Test creation of a list """
        response = self.post()
        self.assertEqual(response.status_code,201)

    def test_getting_all_lists(self):
        """Test getting all lists"""
        self.post()
        user_token = jwt.encode(
            {"email":"kabaki.kiarie@gmail.com"},KEY,
            algorithm='HS256')
        response = self.client.get('/lists',
        headers={'x-access-token': user_token})
        self.assertEqual(response.status_code,200)

    def test_getting_specific_list(self):
        """Test getting specific list"""
        self.post()
        user_token = jwt.encode(
            {"email":"kabaki.kiarie@gmail.com"},KEY,
            algorithm='HS256')
        response = self.client.get('/lists/{}'.format(2),
        headers={'x-access-token': user_token})
        self.assertEqual(response.status_code,200)

    def test_editing_a_list(self):
        """Testing editing a specific list"""
        self.post()
        user_token = jwt.encode(
            {"email":"kabaki.kiarie@gmail.com"},KEY,
            algorithm='HS256')
        response = self.client.patch('/lists/{}/content'.format(2),
            data=json.dumps(self.updated_list),
            headers={'x-access-token': user_token},
            content_type='application/json')
        self.assertEqual(response.status_code,200)
        
    def test_deleting_a_list(self):
        """Testing deleting a specific list"""
        user_token = jwt.encode(
            {"email": "kabaki.kiarie@gmail.com"},KEY,
            algorithm='HS256')
        response = self.client.delete('/lists/{}'.format(1),
            data=json.dumps(self.updated_list),
            headers={'x-access-token': user_token},
            content_type='application/json')
        self.assertEqual(response.status_code,200)
