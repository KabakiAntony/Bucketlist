from . import db
class Lists:
    """Lists model"""
    
    
    def __init__(self,content,user_id):
        """Initialize the members of the posts"""
        self.content = content
        self.user_id = user_id


    def create_post_item(self):
        """create/add a new bucket list item to the
        database"""
        insert_new_post = """
        INSERT INTO posts(content,user_id) VALUES ('{}','{}') RETURNING post_id;
        """.format(self.content,self.user_id)
        return db.handle_other_queries(insert_new_post,True)

    def format_lists(iterable):
        """format the list to make it a dict"""
        list_data = []
        for list_item in iterable:
            list_format = {
                "post_id":list_item[0],
                "content":list_item[1],
                "user_id":list_item[2]
                }
            list_data.append(list_format)
        return list_data

    def get_all_post_items(user_id):
        """Getting all list items"""
        get_all_posts = """
        SELECT post_id, content,user_id from posts
        WHERE posts.user_id ='{}'""".format(user_id)
        return Lists.format_lists(db.handle_select_queries(get_all_posts))

    def get_a_single_post(user_id,post_id):
        """Getting all list items"""
        get_a_single_post_item = """
        SELECT post_id, content, user_id from posts
        WHERE posts.post_id ={} AND posts.user_id={}""".format(post_id,user_id)
        return Lists.format_lists(db.handle_select_queries(get_a_single_post_item))

    def update_a_post(user_id,post_id,update_content):
        """Updating a list item"""
        updating_post_item = """
        UPDATE posts SET  content ='{}' WHERE posts.post_id ={}
        AND posts.user_id={}
        """.format(update_content,post_id,user_id)
        if Lists.get_a_single_post(user_id,post_id):
            db.handle_other_queries(updating_post_item)
            return Lists.get_a_single_post(user_id,post_id)    
    
    def delete_a_post(user_id,post_id):
        """Updating a list item"""
        deleting_a_post_item = """
        DELETE FROM posts  WHERE posts.post_id ={}
        AND posts.user_id={}
        """.format(post_id,user_id)
        if Lists.get_a_single_post(user_id,post_id):
            db.handle_other_queries(deleting_a_post_item)
            return "Post id {} deleted successfully.".format(post_id)
