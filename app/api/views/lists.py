import psycopg2
from flask import request
from app.api import bucket_list
from app.api.models.lists import Lists
from app.api.utils import override_make_response,check_return

@bucket_list.route("/lists",methods=['POST'])
def create_post():
    """This creates a new bucket list item"""
    try:
        post_data = request.get_json()  
        content = post_data["content"]
        user_id = post_data["user_id"]
        new_post = Lists(content=content,user_id = user_id)
        post_id = new_post.create_post_item()
        return override_make_response("Data",[{"content":content,"post_id":post_id}],201)
    except psycopg2.DatabaseError as error:
        return override_make_response("Error",{}.format(error),400)

@bucket_list.route("/lists",methods=['GET'])
def get_all_posts():
    """Get all the lists in the database"""
    return check_return(Lists.get_all_post_items())

@bucket_list.route("/lists/<int:post_id>",methods=['GET'])
def get_a_single_list(post_id):
    """Get all the lists in the database"""
    return check_return(Lists.get_a_single_post(post_id))

@bucket_list.route("/lists/<int:post_id>/content",methods=['PATCH'])
def update_a_post(post_id):
    """This updates a list information"""
    try:
        post_data = request.get_json()
        update_content = post_data["content"]
        return check_return(Lists.update_a_post(post_id,update_content))
    except psycopg2.DatabaseError as error:
        return override_make_response("Error",{}.format(error),400)

@bucket_list.route("/lists/<int:post_id>",methods=['DELETE'])
def delete_a_post(post_id):
    """This deletes a list by supplying it's id"""
    return check_return(Lists.delete_a_post(post_id))
