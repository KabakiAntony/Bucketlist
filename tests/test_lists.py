# all the tests for lists go here.
import unittest 
import json
from app import create_app
from app.api.models.db import db_init
from app.api.models.lists import Lists

class TestLists(unittest.TestCase):
    def setUp(self):
        """Set up tests"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.test_list = {"content": "test list"}
        self.specific_list = {"id":0,"content": "test list"}
        

    def tearDown(self):
        """Clear the db after tests finish running"""
        db_init()
    
    def post(self,data={}):
        """ This is just a helper method for the 
        test cases that need to post data see
        comments for more explanation."""
        if not data:
            data = self.test_list
        response = self.client.post('/bucket/lists'
        ,data=json.dumps(self.test_list), content_type='application/json')
        return response
    
    def test_creating_validated_list(self):
        """Test creation of a list """
        response = self.post()
        self.assertEqual(response.status_code,201)

    def test_getting_all_lists(self):
        """Test getting all lists"""
        response = self.client.get('/bucket/lists')
        self.assertEqual(response.status_code,200)
