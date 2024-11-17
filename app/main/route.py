from flask import Blueprint, flash, get_flashed_messages, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from app.forms.main import SignUpForm
from app.model.subscribers import Subscriber
from ..extensions import db

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    # form = SignUpForm()
    # if form.validate_on_submit():
    #     email = form.email.data
    #     # Handle the email (e.g., save to database or send an email)
    #     flash("Thank you for signing up!", "success")
    #     return redirect(url_for("main.home"))
    return render_template('home.html', title="Coming Soon")

@main.route("/coming-soon", methods=["POST"])
def sign_up():
    email = request.form['email']
    
    # Check if email exists in the database
    existing_subscriber = Subscriber.query.filter_by(email=email).first()
    
    if existing_subscriber:
        # Email already exists
        flash("You have already signed up with this email!", category="error")
    else:
        # Add the new subscriber
        new_subscriber = Subscriber(email=email)
        db.session.add(new_subscriber)
        db.session.commit()
        flash("Thank you for signing up! We will be in touch.", category="success")
    
    # Return the flash message HTML to be appended to the alert container
    return render_template('alert.html', messages=get_flashed_messages(with_categories=True))



@main.route('/about')
def about():
    return render_template('about.html')

@main.route("/test-alert")
def test_alert():
    return render_template("alert.html", message="Test message!", category="success")


