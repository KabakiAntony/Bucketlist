import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')

class Production(Config):
    DATABASE_URI = os.environ.get('PROD_DATABASE_URL')

class Development(Config):
    TESTING = True 
    DATABASE_URI = os.environ.get('TEST_DATABASE_URL')

class Testing(Config):
    DEBUG = True
    DATABASE_URI = os.environ.get('TEST_DATABASE_URL')
