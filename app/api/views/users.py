import os
import jwt
from flask import request,abort,render_template,jsonify
from app.api import bucket_list
from app.api.models.users import User
import psycopg2
from app.api.utils import override_make_response,\
    check_return,is_email_valid,is_valid_password,\
    check_for_details_whitespace,send_mail,token_required


KEY = os.getenv('SECRET_KEY')
url = os.getenv('VERIFY_EMAIL_URL')
link = os.getenv('PASSWORD_RESET_URL')




@bucket_list.route("/auth/signup",methods=['POST'])
def user_signup():
    """Signs a  new user up"""
    try:
        data = request.get_json()
        firstname = data["firstname"]
        email = data["email"]
        password = data["password"]
    except:
        abort(override_make_response("error",
        "Keys should be 'firstname','email','password'",400))
    
    # check if any field is empty
    check_for_details_whitespace(data,["firstname","email","password"])
    # first check if email is valid
    is_email_valid(email)
    # is the email already in use or not
    if User.get_user_by_email(email):
        abort(override_make_response
        ("error","The email is already in use, choose another one",409 ))
    # check if password meets expectations
    is_valid_password(password)
    new_user = User(firstname = firstname,email = email,password = password)
    new_user.create_user()
    token = jwt.encode({"email" :email},KEY,algorithm="HS256")

    # send email on sign up
    subject = """Welcome to Kabucketlist"""
    content = f"""
    Hey {firstname},
    <br/>
    <br/>
    Welcome to kabucketlist, to activate your account<br/>
    please verify your email by clicking on this
    <a href="{url}?in={token.decode('utf-8')}">link</a>.
    <br/>
    <br/>
    Regards Antony,<br/>
    Kabucketlist. 
    """
    send_mail(email,subject,content)
    return override_make_response(
        "data",[{"firstname":firstname,"email":email,"token":token.decode('utf-8')}],201)

@bucket_list.route("/auth/signin",methods=['POST'])
def user_login():
    """Authorize the user to access the system"""
    try:
        data = request.get_json()
        email = data["email"]
        entered_password = data["password"]
    except KeyError:
        abort(override_make_response(
            "error","Keys should be email,password",400))

    # check if any field is empty
    check_for_details_whitespace(data,["email","password"])
    # then check if email is valid
    is_email_valid(email)

    try:
        # see if user exists 
        user = User.get_user_by_email(email)
        if not user:
            abort(override_make_response(
                "error","User not found, please check email.",404))

        # format the returned user
        user_id = user[0][0]
        email = user[0][2]
        returned_password = user[0][3]
        password_check = User.compare_password(returned_password,entered_password)
        if not password_check:
            abort(override_make_response("error","Password is incorrect, please try again",401))

        # check if user has confirmed their email
        if User.is_email_verified(email)[0][0] == 'False':
            abort(override_make_response("error","please confirm your email to sign in",401))

        token = jwt.encode({"email" :email},KEY,algorithm="HS256")
         
        return override_make_response("data",token.decode('utf-8'),200)
    except psycopg2.DatabaseError as _error:
        abort(override_make_response("error", "Server error, contact admin.",500))
    
@bucket_list.route("/users",methods=['GET'])
def get_all_users():
    """List all system users"""
    return check_return(User.get_all_users())


@bucket_list.route("/users/<int:user_id>",methods=['GET'])
def  get_specific_user(user_id):
    """Get a specific user"""
    return check_return(User.get_user_by_id(user_id))

@bucket_list.route("/auth/send-reset",methods=['POST'])
def send_reset():
    """This sends the email instructions on how to reset password """
    try:
        data = request.get_json()
        email = data['email']

    except KeyError:
        abort(override_make_response
        ("error", "Key should be email",400))

    # check if any field is empty
    check_for_details_whitespace(data,["email"])
    # then check if email is valid
    is_email_valid(email)
    # then check if user exists
    user = User.get_user_by_email(email)
    if not user:
        abort(override_make_response
        ("error", "No account associated with that email was found !",404))

    token = jwt.encode({"email" :email},KEY,algorithm="HS256")
    
    # send email on sign up
    subject = """Password reset instructions"""
    content = f"""
    Hey,
    <br/>
    <br/>
    You have requested to reset your password<br/>
    please  click on the following 
    <a href="{link}?in={token.decode('utf-8')}">link</a><br/>
    If you wish to continue with reset, ignore if you did<br/> 
    not initialize the action.
    <br/>
    <br/>
    Regards Antony,<br/>
    Kabucketlist. 
    """
    send_mail(email,subject,content)

    return override_make_response("data",
    f"Password reset instructions sent to {email} successfully",202)

@bucket_list.route("/auth/newpass",methods=['POST'])
def update_password():
    """Update user password"""
    try: 
        data = request.get_json()
        email = data['email']
        password = data['password']

    except KeyError:
        abort(override_make_response
        ("error", "Keys should be email & password",400))
    
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
        ("error", "No account associated with that email was found !",404))
    # if all is ok update user password.
    User.update_password(email,password)

    token = jwt.encode({"email" :email},KEY,algorithm="HS256")
    
    # send email on sign up
    subject = """Password changed successfully."""
    content = f"""
    Hey,
    <br/>
    <br/>
    Your password has been updated successfully.<br/>
    If you did not initialize this action <br/>
    please change your password
    <a href="{link}?in={token.decode('utf-8')}">here</a> 
    <br/>
    <br/>
    Regards Antony,<br/>
    Kabucketlist. 
    """
    send_mail(email,subject,content)

    return override_make_response("data",
    "You have set a new password successfully.",200)


@bucket_list.route("/auth/verify",methods=['GET'])
@token_required
def verify_email(user):
    """verifies signed up user email"""
    email = user[0][1]
    User.verify_email(email)
    return render_template('verify.html')

@bucket_list.route("/u/new-password")
@token_required
def load_reset_ui(user):
    """Loads the ui for reset password"""
    return render_template('new-password.html')

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


        




