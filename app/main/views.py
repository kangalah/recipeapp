
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

    return render_template('recipe.html', recipe=recipe_blog, reviews=reviews)

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

