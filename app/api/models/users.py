# this file will deal with user management
import os
import jwt
import sys
import sendgrid
from . import db
from flask import abort
from sendgrid.helpers.mail import Email, Content, Mail
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """This creates the model for the system users"""
    def __init__(self,firstname,email,password):
        """Initializes the attributes for the class"""
        self.firstname = firstname 
        self.email = email 
        self.password = self.encrypt_password(password)

    def create_user(self):
        """Here we are creating a new system user by adding them into 
        the users table in the database."""
        add_user="""
        INSERT INTO users(firstname,email,password) VALUES
        ('{}','{}','{}') RETURNING user_id;""".format(self.firstname,self.email,self.password)
        return db.handle_other_queries(add_user,True)
    
    def encrypt_password(self,password):
        """Helps to encrypt password"""
        password_hash = generate_password_hash(str(password))
        return password_hash
    
    def compare_password(hashed_password,password):
        """Helps compare a plain string password against its hash
        returns true or false"""
        return check_password_hash(hashed_password,str(password))

    def fromat_users_to_list(iterable):
        """This takes the users returned from
        get all users and returns a list
        """
        users_list = []
        for user in iterable:
            user_dict ={
                "user_id":user[0],
                "firstname":user[1],
                "email":user[2]
            }
        users_list.append(user_dict)
        return users_list

    def get_user_by_email(email):
        """Getting the user against their email address"""
        get_user_by_email= """
        SELECT user_id,firstname,email,password from users 
        where users.email ='{}'""".format(email)
        return db.handle_select_queries(get_user_by_email)

    def get_user_by_id(user_id):
        """Getting the user against their user_id"""
        get_user_by_id= """
        SELECT user_id,firstname,email from users
        where users.user_id ='{}'""".format(user_id)
        returned = db.handle_select_queries(get_user_by_id)
        return User.fromat_users_to_list(returned)
    
    def get_all_users():
        """Getting all users in database"""
        get_all_users ="""
        SELECT * from users"""
        returned = db.handle_select_queries(get_all_users)
        return User.fromat_users_to_list(returned)
    

    
    


