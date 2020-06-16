import os
import sendgrid
from sendgrid.helpers.mail import *
from flask import jsonify,request,make_response,abort
from functools import wraps
from app.api.models.db import handle_select_queries
import jwt
import re
KEY = os.getenv('SECRET_KEY')

def override_make_response(key,message,status):
    """This method overrides make_response making custom responses from
    views it will be available for various versions of the api hence reducing
    the repetition throughout the code for easy readability"""
    raw_dict = {"status":status}
    raw_dict[key] = message
    return make_response(jsonify(raw_dict),status)


def check_return(returned):
    """This method checks what was returned from the models and
    assigns a 404/200 or 201 in the special case of creation
    and assigns it a better message for the user
    """
    if not returned:
        message = "No list was found!"
        status = 404
        response = override_make_response("Error",message,status)
    else:
        message = returned
        status = 200
        response = override_make_response("Data",message,status) 
    return response

def is_email_valid(email):
    """This function checks whether an email is valid"""
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        abort(override_make_response("data","email is invalid",400))
    return True


def is_valid_password(password):
    """Check if the user supplied a password that meets
    expectations"""
    # check the length of the password
    if len(password) < 6 or len(password) > 20:
        abort(
            override_make_response
            ("error","Password should be atleast 6 characters & not exceed 20",400))

    lowercase_reg = re.search("[a-z]", password)
    uppercase_reg = re.search("[A-Z]", password)
    number_reg = re.search("[0-9]", password)
    if not lowercase_reg or not uppercase_reg or not number_reg:
        abort(override_make_response
        ("error","Password should contain at least 1 number, 1 small letter & 1 Capital letter",400))

def check_for_details_whitespace(data, items_to_check):
    """Check whether any of the user details is blank"""
    for key, value in data.items():
        if key in items_to_check and not value.strip():
            abort(override_make_response
            ("error","{} field cannot be left blank".format(key),400))
    return True

def token_required(f):
    """
        This function checks to ensure that a token is supplied
        when accessing certain routes.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'] 
        if not token:
            return override_make_response("Error","Token is missing",401)
        try:
            data = jwt.decode(token,KEY,algorithm="HS256")
            query = """
            SELECT user_id,email FROM users
            WHERE users.email = '{}'""".format(data['email'])
            user = handle_select_queries(query)
        except:
            return override_make_response("Error","Token is expired or invalid",401)
        return f(user, *args, **kwargs)
    return decorated

def send_mail(email,emailSubject,emailContent):
    """
    This sends email on successful sign up / reset password
    """
    try:
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("kabaki.antony@gmail.com","Kabucketlist")
        to_email = To(email)
        subject = emailSubject
        html_content = Content("text/html", emailContent)
        mail = Mail(from_email, to_email, subject, html_content)
        #sg.send(mail)
        response = sg.client.mail.send.post(request_body=mail.get())

        if (response.status_code == 202):
            return override_make_response("data","Success",response.status_code)
        else:
            return override_make_response("error","An error occured",response.status_code)
        #return override_make_response("data",response.body,response.status_code)
    except Exception as e:
        return override_make_response("error",e,400)
    
