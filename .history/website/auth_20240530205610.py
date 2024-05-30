from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password')
        password2 = request.form.get('confirmPassword')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # add user to database
            user = User(email=email, firstName=firstName, password=password1)
            flash('Account created!', category='success')
            # add user to database
            # login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("signup.html")


@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"