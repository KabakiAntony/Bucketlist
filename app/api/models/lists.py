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

    def format_lists(iterable):
        """format the list to make it a dict"""
        list_data = []
        for list_item in iterable:
            list_format = {
                "id":list_item[0],
                "content":list_item[1]
                }
            list_data.append(list_format)
        return list_data


    def get_all_list_items():
        """Getting all list items"""
        get_all_lists = """
        SELECT id, content from list """
        return Lists.format_lists(db.handle_select_queries(get_all_lists))
    