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
        insert_new_post = f"""
        INSERT INTO posts(content,user_id,isStarted,isCompleted)
        VALUES ('{self.content}','{self.user_id}','true','false') RETURNING post_id;
        """
        return db.handle_other_queries(insert_new_post,True)

    def format_lists(self,iterable):
        """format the list to make it a dict"""
        list_data = []
        for list_item in iterable:
            list_format = {
                "post_id":list_item[0],
                "content":list_item[1],
                "user_id":list_item[2],
                "isStarted":list_item[3],
                "isCompleted":list_item[4]
                }
            list_data.append(list_format)
        return list_data

    def get_all_post_items(self,user_id):
        """Getting all list items"""
        get_all_posts = f"""
        SELECT post_id, content,user_id,isStarted,isCompleted from posts
        WHERE posts.user_id ='{user_id}'"""
        return Lists.format_lists(db.handle_select_queries(get_all_posts))

    def get_a_single_post(self,user_id,post_id):
        """Getting all list items"""
        get_a_single_post_item = f"""
        SELECT post_id, content, user_id,isStarted,isCompleted from posts
        WHERE posts.post_id ={post_id} AND posts.user_id={user_id}"""
        return Lists.format_lists(db.handle_select_queries(get_a_single_post_item))

    def update_a_post(self,user_id,post_id,update_content):
        """Updating a list item"""
        updating_post_item = f"""
        UPDATE posts SET  content ='{update_content}' WHERE posts.post_id ={post_id}
        AND posts.user_id={user_id}
        """
        if Lists.get_a_single_post(user_id,post_id):
            db.handle_other_queries(updating_post_item)
            return Lists.get_a_single_post(user_id,post_id)    
    
    def delete_a_post(self,user_id,post_id):
        """Updating a list item"""
        deleting_a_post_item = """
        DELETE FROM posts  WHERE posts.post_id ={post_id}
        AND posts.user_id={user_id}
        """
        if Lists.get_a_single_post(user_id,post_id):
            db.handle_other_queries(deleting_a_post_item)
            return f"Post id {post_id} deleted successfully."
