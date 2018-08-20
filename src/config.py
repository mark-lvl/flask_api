# /src/config.py

import os


class Config(object):
    """
    General environment configuration
    """
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')


class Development(Config):
    """
    Development environment configuration
    """
    TESTING = True


class Production(Config):
    """
    Production environment configuration
    """
    DEBUG = False


app_config = {
    'development': Development,
    'production': Production
}
