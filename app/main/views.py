
from flask import render_template,request,redirect, url_for, abort, flash
from . import main
from .. import db
from ..models import User,Recipe,Review, DbUser
from flask import Flask, render_template, redirect, url_for

from app.main.forms import LoginForm, RegisterForm, RecipeForm
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

from app.main.forms import LoginForm, RegisterForm,RecipeForm


from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


@main.route('/recipe/<int:id>')
def single_recipe(id):

    single_recipe = Recipe.query.get(id)

    reviews = Review.get_reviews(id)

    if single_recipe is None:
        abort (404)


    

    return render_template('recipe.html', recipe = recipe, reviews=reviews)


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



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login',methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():

        user = User.query.filter_by(username=login_form.username.data).first()

        if user:
            if login_user(DbUser(user)):
                    # do stuff
                    flash("You have logged in")
                    return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password')

    

    title = 'Login'
    return render_template('login.html', login_form=login_form, title=title)
        
        
@main.route('/signup',methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method = 'sha256')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.login'))
        # return '<h1>' + form.username.data + ' ' + form.email.data + '' + form.password.data + '</h1>'
    
    return render_template('signup.html', form = form)

@main.route('/addrecipe',methods=['GET', 'POST'])
@login_required
def add_recipe():
    form = RecipeForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            recipe = form.recipe.data
            new_recipe = Recipe(title = title, description = description, recipe = recipe)
            print('new_recipe')
        
            new_recipe.save_recipe()
            
            return redirect(url_for('main.index'))
    
    return render_template('add_recipe.html', form = form)

@main.route('/logout')
@login_required
def logout():

    logout_user()
    return redirect(url_for('main.index'))



@main.route('/contact')
def contact():
    return render_template('contact.html')
