from flask import Blueprint, render_template, render_template_string

users = Blueprint('users', __name__)

@users.route('/users')
def get_users():
    _users = [
        {"id": 1, "name": "monde"},
        {"id": 2, "name": "milani"}
    ]

    return render_template("users/users-list.html", users=_users)