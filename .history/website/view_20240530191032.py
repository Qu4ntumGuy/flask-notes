from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user='user', title='Home')
    # return "<h1>Home</h1>"
