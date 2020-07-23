import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/recipeapp'
    SECRET_KEY = '\xc2\x022\xb86f\xac\xce\x85;\x9f\x14\xb4\xe6zZS\x18t\xb4'
   
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    
    DEBUG = True



config_options = {
    'development':DevConfig,
    'production':ProdConfig
}