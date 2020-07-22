from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class RecipeForm(FlaskForm):
    
    title = StringField('Recipe Title', validators=[Required()])

    description = StringField('Recipe Description', validators=[Required()])

    ingredients = TextAreaField('Ingredients')

    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    
    review = TextAreaField('Recipe Review')

    submit = SubmitField('Submit')

class EditRecipe(FlaskForm):
    
    submit = SubmitField('Edit Recipe')