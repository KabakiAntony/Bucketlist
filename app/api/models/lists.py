from . import db
class Lists:
    """Lists model"""
    
    
    def __init__(self,content):
        """Initialize the members of the lists"""
        self.content = content

    def create_list_item(self):
        """create/add a new bucket list item to the
        database"""
        insert_new_list = """
        INSERT INTO list(content) VALUES ('{}') RETURNING id;
        """.format(self.content)
        return db.handle_other_queries(insert_new_list,True)
    