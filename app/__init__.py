from flask import Flask

def create_app():
    """This is where the app is created for this application"""
    app = Flask(__name__)
    return app

