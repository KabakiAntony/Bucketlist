import sys
import psycopg2
import psycopg2.extras
from flask import current_app as app


def db_init():
    """
    Initialize the database
    """
    try:
        konnection, kursor = db_connection()
        db_init_queries =[]
        if app.config['TESTING']:
            db_init_queries = drop_tables() + create_tables()
            print("*** Tables dropped & created successfully ...")
        else:
            db_init_queries = create_tables()
            print("*** Tables created successfully ....")
        i = 0
        while i != len(db_init_queries):
            query = db_init_queries[i]
            kursor.execute(query)
            konnection.commit()
            i += 1
        konnection.close()
    except Exception as error:
        print("We got an error of ->:{} @method db_init".format(error))

def create_tables():
    """
    Create the tables that will hold
    all the data for this simple app
    """
    create_users_table ="""
    CREATE TABLE IF NOT EXISTS users
    (
        user_id SERIAL PRIMARY KEY,
        firstname varchar(25) NOT NULL,
        email VARCHAR (30) NOT NULL UNIQUE,
        password VARCHAR (128) NOT NULL
    )"""

    create_posts_table ="""
    CREATE TABLE IF NOT EXISTS posts
    (
        post_id SERIAL PRIMARY KEY,
        content varchar(255) NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
    )"""
    return [create_users_table,create_posts_table]


def drop_tables():
    """Drop tables everytime the app restarts"""
    drop_users_table ="""
    DROP TABLE IF EXISTS users CASCADE"""
    drop_posts_table ="""
    DROP TABLE IF EXISTS posts CASCADE"""
    return [drop_users_table,drop_posts_table]


def db_connection(query=None):
    """
    Try connecting to the database if successful
    return the connection and the cursor object
    """
    konnection = None
    kursor = None
    DB_URL = app.config["DATABASE_URI"]
    try:
        konnection = psycopg2.connect(DB_URL)
        kursor = konnection.cursor(cursor_factory=psycopg2.extras.DictCursor)    
        if query:
            kursor.execute(query)
            konnection.commit()

    except (Exception,psycopg2.DatabaseError) as error:
        print("We got an error of ->:{}  @method db_connection".format(error))
    return konnection, kursor


def handle_other_queries(query,isquery=False):
    """Handles insert/patch/delete queries"""
    konnection,kursor = db_connection(query)
    try:
        if isquery:
            get_last_insert = kursor.fetchone()[0]
            konnection.close()
            return get_last_insert
        konnection.close()
    except psycopg2.Error as error:
        print("We got an error of ->: {} @method handle_other_queries.".format(error))
        sys.exit(1)

def handle_select_queries(query):
    """Handle select queries"""
    rows = None
    konnection, kursor = db_connection(query)
    if konnection:
        rows = kursor.fetchall()
        konnection.close()
    return rows