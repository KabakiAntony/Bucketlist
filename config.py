import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URI = os.environ.get('PROD_DATABASE_URL')

class Production(Config):
    pass

class Development(Config):
    TESTING = True 

class Testing(Config):
    DEBUG = True
    DATABASE_URI = os.environ.get('PROD_DATABASE_URL')


app_config = {
    "development": Development,
    "testing": Testing
}