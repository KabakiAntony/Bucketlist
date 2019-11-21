from flask import jsonify,request,make_response

def override_make_response(key,message,status):
    """This method overrides make_response making custom responses from
    views it will be available for various versions of the api hence reducing
    the repetition throughout the code for easy readability"""
    raw_dict = {"Status":status}
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
 
