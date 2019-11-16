from flask import Flask
from config import app_config
from app.api.views.lists import bucket_list
#from app.api.models.db import db_init

def create_app(the_configuration):
    """This is where the app is created for this application"""
    app = Flask(__name__)
    app.config.from_object(app_config[the_configuration])
    app.app_context().push()
    app.register_blueprint(bucket_list)
    #if the_configuration != "testing":
    #  db_init()
    return app

