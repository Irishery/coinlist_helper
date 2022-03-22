from flask import Blueprint, jsonify, request
from app import db
from app.models import User


user_api = Blueprint('user_api', __name__)


@user_api.route('/api/user/<int:id>', methods=["GET"])
def get_user(id):
    return jsonify(User.query.filter_by(id=id).first())

@user_api.route('/api/users', methods=["GET"])
def get_users():
    return jsonify(User.query.all())

@user_api.route('/api/user/<int:id>', methods=["DELETE"])
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.query(User).filter(User.id==id).first()
    db.session.commit()
    return jsonify(user)

@user_api.route('/api/user/<int:id>', methods=["POST"])
def post_user(id):
    content = request.json
    print(content)

@user_api.route('/api/user/<int:id>', methods=["PUT"])
def update_user(id):
    content = request.json
    print(content)
