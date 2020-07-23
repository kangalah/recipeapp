from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length, Required

# class RecipeForm(FlaskForm):
    
#     title = StringField('Recipe Title', validators=[Required()])

#     description = StringField('Recipe Description', validators=[Required()])

#     ingredients = TextAreaField('Ingredients')

#     submit = SubmitField('Submit')

# class ReviewForm(FlaskForm):
    
#     review = TextAreaField('Recipe Review')

#     submit = SubmitField('Submit')

# class EditRecipe(FlaskForm):
    
#     submit = SubmitField('Edit Recipe')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min = 4, max = 15)])
    password = PasswordField('password', validators = [InputRequired(), Length(min = 8, max = 80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators = [InputRequired(), Length(min = 8, max = 80)])