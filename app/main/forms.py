from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length, Required


class AddRecipeForm(FlaskForm):
    recipe_title = StringField('Recipe Title', validators=[Required()])
    recipe_description = StringField('Recipe Description', validators=[Required()])

class LoginForm(FlaskForm):
    username = StringField('username', validators=[Required()])
    password = PasswordField('password', validators = [Required()])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[Required()])
    username = StringField('username', validators=[Required()])
    password = PasswordField('password', validators = [Required()])