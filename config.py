import tempfile
import os


class Config(object):
    DEBUG = os.getenv('DEBUG', False)
    TESTING = False
    PORT = os.getenv('PORT', 8001)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI',
                                        'sqlite:///' + os.path.join(tempfile.gettempdir(), 'categories.db'))
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
