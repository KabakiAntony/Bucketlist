import psycopg2
from flask import request
from app.api import bucket_list
from app.api.models.lists import Lists
from app.api.utils import override_make_response,check_return

@bucket_list.route("/lists",methods=['POST'])
def create_list():
    """This creates a new bucket list item"""
    try:
        list_data = request.get_json()  
        content = list_data["content"]
        new_list = Lists(content=content)
        list_id = new_list.create_list_item()
        return override_make_response("Data",[{"content":content,"id":list_id}],201)
    except psycopg2.DatabaseError as error:
        return override_make_response("Error",{}.format(error),400)

@bucket_list.route("/lists",methods=['GET'])
def get_all_lists():
    """Get all the lists in the database"""
    return check_return(Lists.get_all_list_items())

@bucket_list.route("/lists/<int:list_id>",methods=['GET'])
def get_a_single_list(list_id):
    """Get all the lists in the database"""
    return check_return(Lists.get_a_single_list(list_id))

@bucket_list.route("/lists/<int:list_id>/content",methods=['PATCH'])
def update_a_list(list_id):
    """This updates a list information"""
    try:
        list_data = request.get_json()
        update_content = list_data["content"]
        return check_return(Lists.update_a_list(list_id,update_content))
    except psycopg2.DatabaseError as error:
        return override_make_response("Error",{}.format(error),400)

@bucket_list.route("/lists/<int:list_id>",methods=['DELETE'])
def delete_a_list(list_id):
    """This deletes a list by supplying it's id"""
    return check_return(Lists.delete_a_list(list_id))
