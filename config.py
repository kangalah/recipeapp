import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/recipeapp'
   
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    
    DEBUG = True



config_options = {
    'development':DevConfig,
    'production':ProdConfig
}