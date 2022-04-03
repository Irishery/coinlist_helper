from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from app.models import User
from app.forms.edit_data import EditProfile
from app import db

main_route = Blueprint("main_route", __name__)

@main_route.route("/")
def base():
    return redirect(url_for('main_route.main'))

@main_route.route("/main", methods=["GET", "POST"])
@login_required
def main():
    data = request.form.to_dict()
    print(data)

    db.session.query(User).\
       filter(User.login == data['login']).\
       update(data)
    db.session.commit()

    return render_template("main.html", title="coinlist", users=User.query.all())

@main_route.route("/table", methods=["GET"])
def table():
    return render_template("table.html")

@main_route.route("/profile", methods=["GET"])
@login_required
def profile():
    form = EditProfile()
    cols = current_user.__mapper__.attrs.keys()[1:]
    return render_template("profile.html", cols=cols, user=current_user,
                                              form=form)

@main_route.route("/profile", methods=["POST"])
@login_required
def edit_rofile():
    form = EditProfile()
    data = form.data
    
    data.pop('csrf_token', None)
    data.pop('save', None)

    db.session.query(User).\
       filter(User.login == data['login']).\
       update(data)
    db.session.commit()

    cols = current_user.__mapper__.attrs.keys()[1:]
    return render_template("profile.html", cols=cols, user=current_user,
                                              form=form)

@main_route.route("/profile", methods=["PUT"])
@login_required
def edit_profile():
    return redirect(url_for("main_route.profile"))
