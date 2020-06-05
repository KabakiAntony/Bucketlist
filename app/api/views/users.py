import os
import jwt
from flask import request,abort,render_template
from app.api import bucket_list
from app.api.models.users import User
import psycopg2
from app.api.utils import override_make_response,\
    check_return,is_email_valid,is_valid_password,\
    check_for_details_whitespace



# the reason I have setup a secret key backup is a work around
# prevent flask from throwing an error of NONETYPE when parsing
# KEY in jwt.encode 
KEY = os.getenv('SECRET_KEY','aX5bqx7djw3Hm1pAz2N8DQOzX3s')


@bucket_list.route("/auth/signup",methods=['POST'])
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
        ("Error","The email is already in use choose another one",409 ))
    # check if password meets expectations
    is_valid_password(password)
    new_user = User(firstname = firstname,email = email,password = password)
    user_id = new_user.create_user()
    return override_make_response(
        "Data",[{"firstname":firstname,"email":email,"user_id":user_id}],201)

@bucket_list.route("/auth/signin",methods=['POST'])
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
        "token": token.decode('utf-8'),
        "user": {"user_id": user_id,"email": email}}],200)
    except psycopg2.DatabaseError as _error:
        abort(override_make_response("Error", "Server error",500))
    
@bucket_list.route("/users",methods=['GET'])
def get_all_users():
    """List all system users"""
    return check_return(User.get_all_users())


@bucket_list.route("/users/<int:user_id>",methods=['GET'])
def  get_specific_user(user_id):
    """Get a specific user"""
    return check_return(User.get_user_by_id(user_id))

@bucket_list.route("/auth/newpass",methods=['POST'])
def update_password():
    """Update user password"""
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']

    except KeyError:
        abort(override_make_response
        ("Error", "Should be email & password",400))
    
    # check if any field is empty
    check_for_details_whitespace(data,["email","password"])
    # then check if email is valid
    is_email_valid(email)
    # then check if password is valid
    is_valid_password(password)
    # then check if user exists
    user = User.get_user_by_email(email)
    if not user:
        abort(override_make_response
        ("Not Found", "User is not registered.",404))
    # if all is ok update user password.
    User.update_password(email,password)

    return override_make_response("Data",
    "Password changed successfully, Login with new password",200)


@bucket_list.route('/u/signup')
def user_signin():
    """Return the user sign up  page"""
    return render_template('signup.html')

@bucket_list.route('/contact')
def contact():
    """Return the contact us page"""
    return render_template('contact.html')

@bucket_list.route('/u/reset')
def password_reset():
    """Return password reset html"""
    return render_template('reset.html')


# @bucket_list.route("/auth/confirm/<token>",methods=['POST'])
# def confirm_email(token):
#     """verifies signed up user email"""

        




