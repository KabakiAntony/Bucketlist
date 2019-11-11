import os
import psycopg2
import psycopg2.extras


konnection = None
kursor = None
DB_URL = os.environ.get('PROD_DATABASE_URL')

def db_init():
    """
    Initialize the database
    """
    db_connection()
    create_table()

def db_connection():
    """
    Try connecting to the database if successful 
    return the connection and the cursor object
    """
    try:
        konnection = psycopg2.connect(DB_URL)
        kursor = konnection.cursor()

    except (Exception,psycopg2.DatabaseError) as error:
        print(f"We got this {error}  while connecting to the database")
    return konnection, kursor


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
    )
    """
    try:
        kon, kursor = db_connection()
        print("Database connection successful.")
        kursor.execute(create_list_table)
        kon.commit()
    except (Exception,psycopg2.DatabaseError) as error:
        print(f"We could not create table due to -> {error}")




