from crypt import methods
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import rbac

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
