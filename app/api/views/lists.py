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
    


