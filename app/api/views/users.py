# this will return and format calls to the user database 
# make it better for view  to user


from flask import request,abort
from app.api import bucket_list
from app.api.models.users import User
import psycopg2
from app.api.utils import override_make_response,\
    check_return,is_email_valid,is_valid_password,\
    check_for_details_whitespace
import requests
import json
import os
import jwt

KEY = os.getenv('SECRET_KEY',"aX5bqx7djw3Hm1pAz2N8DQOzX3s")


@bucket_list.route("/signup",methods=['POST'])
def user_signup():
    """Signs a  new user up"""
    try:
        data = request.get_json()
        firstname = data["firstname"]
        email = data["email"]
        password = data["password"]
    except:
        abort(override_make_response("Error",
        "Keys should be 'firstname','email','password'",400))
    
    # check if any field is empty
    check_for_details_whitespace(data,["firstname","email","password"])
    # first check if email is valid
    is_email_valid(email)
    # is the email already in use or not
    if User.get_user_by_email(email):
        abort(override_make_response
        ("Error","The email is already in use choose another one",400))
    # check if password meets expectations
    is_valid_password(password)
    new_user = User(firstname = firstname,email = email,password = password)
    user_id = new_user.create_user()
    return override_make_response(
        "Data",[{"firstname":firstname,"email":email,"user_id":user_id}],201)

@bucket_list.route("/signin",methods=['POST'])
def user_login():
    """Authorize the user to access the system"""
    try:
        data = request.get_json()
        email = data["email"]
        entered_password = data["password"]
    except KeyError:
        abort(override_make_response(
            "Error","Keys should be email,password",400))

    # check if any field is empty
    check_for_details_whitespace(data,["email","password"])
    # then check if email is valid
    is_email_valid(email)

    try:
        # see if user exists 
        user = User.get_user_by_email(email)
        if not user:
            abort(override_make_response(
                "Error","User does not exist, Please check email.",404))

        # format the returned user
        user_id = user[0][0]
        email = user[0][2]
        returned_password = user[0][3]
        password_check = User.compare_password(returned_password,entered_password)
        if not password_check:
            abort(override_make_response("Error","The password is wrong, please try again",400))

        token = jwt.encode({"email" :email},KEY,algorithm="HS256")
        return override_make_response("Data",
        [{"message": "Logged in successfully",
        "token": token.decode("UTF-8"),
        "user": {"user_id": user_id,"email": email}}],200)
    except psycopg2.DatabaseError as _error:
        abort(override_make_response("Error", "Server error",500))
        




