from flask import Flask, render_template
from flask_login import LoginManager
from flask_mail import Mail

import os

app=Flask(
    __name__, instance_path=os.path.join(os.path.abspath(os.curdir), 'instance'),
    instance_relative_config=True
)

mail=Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='users.login'

from app.user.views import users_blueprint

app.register_blueprint(users_blueprint)