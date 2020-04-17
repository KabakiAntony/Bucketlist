from flask import Flask
from config import app_config
from app.api.views.lists import bucket_list as lists_blueprint
from app.api.views.users import bucket_list as users_blueprint
from app.api.models.db import db_init
from flask_cors import CORS

def create_app(the_configuration):
    """This is where the app is created for this application"""
    app = Flask(__name__)
    #enable cross origin rekuests
    CORS(app)
    app.config.from_object(app_config[the_configuration])
    app.app_context().push()
    app.register_blueprint(lists_blueprint)
    app.register_blueprint(users_blueprint)
    if the_configuration != "testing":
        db_init()
    return app

