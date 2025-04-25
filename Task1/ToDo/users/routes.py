from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import login_user, current_user, logout_user
from ToDo.users.forms import RegistrationForm, LoginForm
from ToDo.models import User
from ToDo import bcrypt, db



users = Blueprint("users", __name__)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f"Welcome {user.username}", "success")
            return redirect(url_for("main.index"))
        else:
            flash(f"Invalid Credentials", "danger")
    return render_template("login.html", title="login", form=form)


@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password_hash.data).decode(
            "utf-8"
        )
        user = User(
            username=form.name.data,
            email=form.email.data,
            password_hash=hashed_password,
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for("users.login"))
    return render_template("register.html", title="register", form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("users.login"))