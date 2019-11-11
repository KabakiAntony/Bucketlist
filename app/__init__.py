from flask import Flask
from app.api.models.db import db_init

def create_app():
    """This is where the app is created for this application"""
    app = Flask(__name__)
    db_init()
    if app.config["ENV"] == "production":
        app.config.from_object("config.Production")
    elif app.config["ENV"] == "development":
        app.config.from_object("config.Development")
    else:
        app.config.from_object("config.Testing")
    return app

