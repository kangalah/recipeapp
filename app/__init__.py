from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from flask_mail import Mail
from flask_uploads import UploadSet,IMAGES, configure_uploads


import  os

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.index'

simple = SimpleMDE()

def create_app(config_name):
    
    app = Flask(__name__,instance_relative_config=True)
    # app.config.from_pyfile('flask.cfg')

    # creating configurations
    app.config.from_object(config_options[config_name])
    # app.config['UPLOADS_DEFAULT_DEST'] = os.path.join('app', 'static', 'img')
    # images = UploadSet('images',IMAGES)
    
    # configure_uploads(app, images)


    # initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail = Mail(app)


    simple.init_app(app)

    # registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app