import os
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
            db_init_queries = drop_list_table() + create_table()
        else:
            db_init_queries = create_table()
        i = 0
        while i != len(db_init_queries):
            query = db_init_queries[i]
            kursor.execute(query)
            konnection.commit()
            i += 1
        print("Database initialized successfully")
        konnection.close()
    except Exception as error:
        print(f"We got an error of ->:' {error} ' while trying to initialize the database.")

def create_table():
    """
    Create the list table that will hold
    all the data for this simple app
    """
    create_list_table ="""
    CREATE TABLE IF NOT EXISTS list
    (
        id SERIAL PRIMARY KEY,
        content varchar(255) not null
    )"""
    return [create_list_table]

def drop_list_table():
    """Drop list table everytime the app restarts"""
    drop_table ="""
    DROP TABLE IF EXISTS list CASCADE"""
    return [drop_table]


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
        # print("\n\nConnected to the database successfully\n")
        kursor = konnection.cursor(cursor_factory=psycopg2.extras.DictCursor)    

        if query:
            kursor.execute(query)
            konnection.commit()

    except (Exception,psycopg2.DatabaseError) as error:
        print(f"We got an error of ->:' {error} ' trying to connect to the database.")
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
        print(f"We got an error of ->:' {error} ' trying to handle other queries.")
        sys.exit(1)

def handle_select_queries(query):
    """Handle select queries"""
    rows = None
    konnection, kursor = db_connection(query)
    if konnection:
        rows = kursor.fetchall()
        konnection.close()
    return rows
        

