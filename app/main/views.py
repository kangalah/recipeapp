
from flask import render_template,request,redirect, url_for, abort
from . import main
from .. import db
from flask_login import login_required
from ..models import User,Recipe,Review
from .forms import ReviewForm, RecipeForm, EditRecipe



@main.route('/')
def index():
    return render_template('index.html') 

@main.route('/recipe/<int:id>')
def single_recipe(id):

    single_recipe = Recipe.query.get(id)

    reviews = Review.get_reviews(id)

    if single_recipe is None:
        abort (404)

    return render_template('recipe.html', recipe=single_recipe, reviews=reviews)

@main.route('/recipe/review/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):

    recipe = Recipe.query.filter_by(id=id).first()

    if recipe is None:
        abort(404)

    form = ReviewForm()

    if form.validate_on_submit():

        review = form.review.data

        new_review = Review(review=review, user_id=current_user.id, recipe_id=recipe.id)

        new_review.save_review()

        return redirect(url_for('.single_recipe', id=recipe.id))

    return render_template('new_review.html', review_form=form, recipe=recipe)

# @main.route('/add', methods=['GET', 'POST'])
# @login_required
# def add_recipe():
#     form = AddRecipeForm()
#     # if request.method == 'POST':
#     if form.validate_on_submit():
#         content = form.content.data
#         new_recipe= Recipe(content=content, recipe_title = recipe.title, recipe_description = recipe.description, recipe_ingredients = recipe.ingredients, user_id = current_user.id)
#         new_recipe.save_recipe()
#         flash('New recipe, {}, added!'.format(new_recipe.recipe_title), 'success')
#         return redirect(url_for('.index'))
#     else:
#         flash_errors(form)
#         flash('ERROR! Recipe was not added.', 'error')
 
#     return render_template('add_recipe.html', form=form)

