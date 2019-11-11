import os
import psycopg2
import psycopg2.extras
from flask import current_app as app


konnection = None
kursor = None
DB_URL = app.config["DATABASE_URI"]
#DB_URL = os.environ.get('PROD_DATABASE_URL')
try:
    konnection = psycopg2.connect(DB_URL)
    kursor =konnection.cursor()
    print("Database connection successful.")
except (Exception,psycopg2.DatabaseError) as error:
    print(f"We got this {error}  while connecting to the database")
