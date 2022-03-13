from flask import Blueprint

main_route = Blueprint('main_route', __name__)


@main_route.route('/')
def hello():
    return 'Hello'
