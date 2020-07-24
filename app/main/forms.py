from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length, Required

class RecipeForm(FlaskForm):


    title = StringField('Recipe Title', validators=[Required()])

    description = StringField('Recipe Description', validators=[Required()])

    recipe = TextAreaField('Recipe')

    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min = 4, max = 15)])
    password = PasswordField('password', validators = [InputRequired()])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators = [InputRequired()])

