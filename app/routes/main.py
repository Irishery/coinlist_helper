from crypt import methods
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import rbac
from app.models import User
from app.routes.route_utils import object_as_dict

main_route = Blueprint("main_route", __name__)

@main_route.route("/")
def base():
    return "This page does not exists"

@main_route.route("/profile", methods=['GET', 'POST'])
# @rbac.deny(['anonymous'], ['GET'])
# @rbac.allow(['user', 'admin'], ['GET', 'POST'])
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)

@main_route.route("/main", methods=["GET", "POST"])
@login_required
def main():
    return render_template("main.html", title="coinlist", users=User.query.all())

@main_route.route("/table", methods=["GET"])
def table():
    return render_template("table.html")
