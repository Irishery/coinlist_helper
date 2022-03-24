from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..forms.authorization import SignUp, SignIn
from flask_login import current_user, login_required, login_user, logout_user
from ..models import User, Role
from app import db, authorize
from werkzeug.security import check_password_hash

auth_route = Blueprint('auth', __name__)


@auth_route.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignUp()
    if request.method == "POST":
        if form.validate_on_submit():
            check_login = User.query.filter_by(login=form.login.data).first()

            if check_login:
                flash('Login already exists')
                return redirect(url_for('auth.sign_up'))
            
            if len(form.password.data) < 3:
                flash('The password is too short')
                return redirect(url_for('auth.sign_up'))

            user = User(platform=form.platform.data, name=form.name.data,
                        login=form.login.data, password=form.password.data)
            role = Role.query.filter_by(name='user').first()
            user.roles.append(role)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for("main_route.main"))
    return render_template("authorization.html", title="authorization",
                                                 form=form, action="sign_up")

@auth_route.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = SignIn()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(login=form.login.data).first()
            if not user or not check_password_hash(user.password,
                                                         form.password.data):
                flash("Login or password is incorrect")
                return redirect(url_for('auth.sign_in'))
            
            login_user(user, remember=form.remember.data)
            return redirect(url_for("main_route.main"))
    return render_template("authorization.html", title="authorization",
                                                 form=form, action="sign_in")


@auth_route.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main_route.main"))
