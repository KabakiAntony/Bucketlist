import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

class Production(Config):
    DATABASE_URI = os.environ.get('PROD_DATABASE_URL')

class Development(Config):
    DEBUG = True

class Testing(Config):
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('TEST_DATABASE_URL')
