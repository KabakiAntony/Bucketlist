import psycopg2
from flask import request
from app.api import bucket_list
from app.api.models.lists import Lists
from app.api.utils import override_make_response,check_return,token_required

@bucket_list.route("/lists",methods=['POST'])
@token_required
def create_post(user):
    """This creates a new bucket list item"""
    try:
        user_id = user[0][0]
    except:
        return override_make_response("error","You don't have an account",401)
    try:
        post_data = request.get_json()  
        content = post_data["content"]
        new_post = Lists(content=content,user_id=user_id)
        post_id = new_post.create_post_item()
        return override_make_response("data",[{"content":content,"post_id":post_id}],201)
    except psycopg2.DatabaseError as error:
        return override_make_response("error",f"{error}",400)

@bucket_list.route("/lists",methods=['GET'])
@token_required
def get_all_posts(user):
    """Get all the lists in the database"""
    try:
        user_id = user[0][0]
        return check_return(Lists.get_all_post_items(user_id))
    except:
        return override_make_response("error","You have not made any posts.",404)

@bucket_list.route("/lists/<int:post_id>",methods=['GET'])
@token_required
def get_a_single_list(user,post_id):
    """Get all the lists in the database"""
    try:
        user_id = user[0][0]
        return check_return(Lists.get_a_single_post(user_id,post_id))
    except:
        return override_make_response("error","Your post has not been found.",404)
    

@bucket_list.route("/lists/<int:post_id>/content",methods=['PATCH'])
@token_required
def update_a_post(user,post_id):
    """This updates a list information...."""
    try:
        user_id = user[0][0]
    except:
        return override_make_response("error","An error occured !",400)
    try:
        post_data = request.get_json()
        update_content = post_data["content"]
        return check_return(Lists.update_a_post(user_id,post_id,update_content))
    except psycopg2.DatabaseError as error:
        return override_make_response("error",f'{error}',400)

@bucket_list.route("/lists/<int:post_id>",methods=['DELETE'])
@token_required
def delete_a_post(user,post_id):
    """This deletes a list by supplying it's id"""
    try:
        user_id = user[0][0]
        return check_return(Lists.delete_a_post(user_id,post_id))
    except:
        return override_make_response("error","An error occurred !",400)
