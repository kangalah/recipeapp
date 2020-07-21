from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), index = True)
    email = db.Column(db.String(250), unique=True, index=True)
    password_hash = db.Column(db.String(400))
    recipe_id = db.relationship('Recipe', backref='user', lazy='dynamic')
    review_id = db.relationship('Review', backref='user', lazy='dynamic')
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('Access Denied!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'

class Recipe(db.Model):
    
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    recipe = db.Column(db.String)
    description = db.Column(db.String)
    ingredients = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.now(tz=None))
    review_id = db.relationship('Review', backref='recipe', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_recipe(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_recipe(cls, id):
        recipes = Recipe.query.order_by(Recipe.posted.desc()).all()
        return recipes

    @classmethod
    def delete_recipe(self, blog_id):
        reviews = Review.query.filter_by(recipe_id=recipe_id).delete()
        recipe = Recipe.query.filter_by(id=recipe_id).delete()
        db.session.commit()

    @classmethod
    def edit_recipe(self, recipe_id):

        recipe = Review.query.filter_by(id=recipe_id).edit()

        db.session.commit()

class Review(db.Model):
    
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)

    review = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.now(tz=None))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls, id):
        reviews = Review.query.filter_by(recipe_id=id).all()
        return reviews

    @classmethod
    def delete_review(self, review_id):

        review = Review.query.filter_by(id=review_id).delete()

        db.session.commit()