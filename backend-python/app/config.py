import os

class Config(object):
#    SECRET_KEY = os.environ.get("flask_key")
    SECRET_KEY = "CONFIGURATION"
    
class DevelopmentConfig(Config):
    DEBUG = True
    

class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


app_config = {'development':DevelopmentConfig}