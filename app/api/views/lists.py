import psycopg2
from app.api import bucket_list
from app.api.models.lists import Lists
from flask import request,jsonify,make_response

@bucket_list.route("/lists",methods=['POST'])
def create_list():
    """This creates a new bucket list item"""
    try:
        list_data = request.get_json()  
        content = list_data["content"]
        new_list = Lists(content=content)
        list_id = new_list.create_list_item() 
        return make_response(jsonify({"content":content,"id":list_id}),201)       
    except psycopg2.DatabaseError as error:
        return make_response(jsonify({f'"Error":[{error}]'}),400)


@bucket_list.route("/lists",methods=['GET'])
def get_all_lists():
    """Get all the lists in the database"""
    return make_response(jsonify(Lists.get_all_list_items()),200)

@bucket_list.route("/lists/<int:list_id>",methods=['GET'])
def get_a_single_list(list_id):
    """Get all the lists in the database"""
    return make_response(jsonify(Lists.get_a_single_list(list_id)),200)

@bucket_list.route("/lists/<int:list_id>/content",methods=['PATCH'])
def update_a_list(list_id):
    """This updates a list information"""
    try:
        list_data = request.get_json()  
        update_content = list_data["content"]
        return make_response(jsonify(Lists.update_a_list(list_id,update_content)),201)       
    except psycopg2.DatabaseError as error:
        return make_response(jsonify({f'"Error":[{error}]'}),400)