import os

from dotenv import load_dotenv
load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URI = os.environ.get('DATABASE_URL')

class Production(Config):
    pass

class Development(Config):
    DEBUG = True
    TESTING = True 
    DATABASE_URI = os.environ.get('TEST_DATABASE_URL')

class Testing(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('TEST_DATABASE_URL')


app_config = {
    "production":Production,
    "development": Development,
    "testing": Testing
}