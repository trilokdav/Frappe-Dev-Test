from flask import Blueprint, render_template, flash, session, Flask

user = Blueprint('user', __name__, template_folder='../assets/templates/user', static_folder='../assets/static', url_prefix="/user")

# from app import mysql


@user.route('/')
def test():
    return render_template('user_dashboard.html')