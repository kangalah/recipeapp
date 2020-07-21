from flask import abort
from flask import Blueprint
from flask import render_template
from flask_login import current_user, login_user, login_required,logout_user
from app import app, mail
from .forms import EmailForm,LoginForm, PasswordForm, RegisterForm

users_blueprint=Blueprint('users',__name__)

@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_user = User(form.email.data, form.password.data)
                new_user.authinticated = True
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering :)', 'Welcome')
                return redirect(url_for('templates.index'))
            except IntegrityError:
                db.session.rollback()
                flash('Error!! Email ({}) already exists.'.format(form.email.data), 'error')
        return render_template('register.html', form=form)
