import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/recipeapp'
    SECRET_KEY = '\x15\x90\x8ff\xc0\xde\xb4\x9bl,\xe9\x8b'
   
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    
    DEBUG = True



config_options = {
    'development':DevConfig,
    'production':ProdConfig
}