from flask import Blueprint, render_template, redirect, url_for, flash, session, request, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from ..models import db, User
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm

# Blueprint setup
auth_bp = Blueprint('auth', __name__)

# Forms
class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Create Account')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already exists!')
            return redirect(url_for('auth.signup'))
        user = User(
            email=form.email.data,
            password=generate_password_hash(form.password.data),
            credits=5
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Welcome! You have 5 free credits.')
        return redirect(url_for('ai.dashboard'))
    return render_template('signup.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('ai.dashboard'))
        flash('Wrong email or password!')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!')
    return redirect(url_for('auth.login'))