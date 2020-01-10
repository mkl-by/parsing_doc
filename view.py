from app import app, login_manager
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user
from forms import Form_login
from app import db
from models import User


@app.route("/")
@login_required
def index():
    name = 'Vasja'
    return render_template('index.html', name=name)


@app.route('/login/', methods=['post', 'get'])
def login():
    form = Form_login()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.chek_passw(form.passw.data):
            login_user(user, force=True)
            flash('вы зарегистрированы', 'bg-success')
            return redirect(url_for('index'))

        # flash("Invalid username/password")

    return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))