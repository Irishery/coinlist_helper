from flask import Blueprint, render_template, request, flash, abort, redirect, url_for
from ..forms.authorization import SignUp, SignIn
from flask_login import login_user
from ..models import User
from .utils import is_safe_url
from app import db

main_route = Blueprint('main_route', __name__)


@main_route.route('/')
def base():
    return "THIS PAGE DOES NOT EXISTS"



@main_route.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignUp()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User(platform=form.platform.data, name=form.name.data,
                        login=form.login.data, password=form.password.data)
            
            db.session.add(user)
            db.session.commit()

            return "ALLRIGHT"
    return render_template("authorization.html", title="authorization",
                                                 form=form, action="sign_up")

@main_route.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    user = User()
    form = SignIn()
    if request.method == "POST":
        if form.validate_on_submit():
            print(form)
            # login_user(user)
            flash("Logged in successfully.")

    return render_template("authorization.html", title="authorization",
                                                 form=form, action="sign_in")
# if request.method == "POST":
#         if form.validate_on_submit():
#             user = User(platform=form.platform.data, name=form.name.data,
#                         login=form.login.data, password=form.password.data)
#             login_user(user)

#             flash("Logged in successfully.")
            
#             next = request.args.get("next")
#             if not is_safe_url(next):
#                 return abort(400)

#         return redirect(next or url_for("/"))
#     return render_template("authorization.html", title="authorization",
#                                                  form=form, action="sign_up")
