
from flask import render_template,request,redirect, url_for, abort, flash
from . import main
from .. import db
from ..models import User,Recipe,Review
from flask import Flask, render_template, redirect, url_for
from app.main.forms import LoginForm, RegisterForm

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
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)

            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username and/or password')

    title = 'Login'
    return render_template('login.html', form=form, title=title)
        
        
@main.route('/signup',methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method = 'sha256')
        new_user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.login'))
        # return '<h1>' + form.username.data + ' ' + form.email.data + '' + form.password.data + '</h1>'
    
    return render_template('signup.html', form = form)

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name = current_user.username)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
