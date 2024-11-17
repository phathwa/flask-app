from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from ..extensions import db, bcrypt
from app.forms.users import LoginForm, RegistrationForm
from app.models import User

users = Blueprint('users', __name__)

@users.route('/users')
def get_users():
    _users = [
        {"id": 1, "name": "monde"},
        {"id": 2, "name": "milani"}
    ]
    return render_template("users/users-list.html", users=_users)

@users.route('/all')
def get_all_users():
    users = User.query.all()  # Get all users from the database
    
    # Convert users to JSON format
    users_list = [{
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'firstname': user.firstname,
        'lastname': user.lastname
    } for user in users]
    
    return jsonify(users_list)  # Return the list as JSON

@users.route("/sign-up", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            firstname=form.firstname.data,  # Save firstname
            lastname=form.lastname.data     # Save lastname
        )
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.home'))
    return render_template('users/sign-up.html', title='Sign Up', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('users/login.html', title='Login', form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))