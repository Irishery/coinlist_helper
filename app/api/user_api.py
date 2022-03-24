from flask import Blueprint, jsonify, request
from flask_restful import Resource
from sqlalchemy import delete
from collections import namedtuple
from app import db
from app.models import User, UserRole


user_api = Blueprint('user_api', __name__)


@user_api.route('/api/user/', methods=["GET"])
def get_user():
    id = request.args.get('id')
    return jsonify(User.query.filter_by(id=id).first())

@user_api.route('/api/users', methods=["GET"])
def get_users():
    return jsonify(User.query.all())

@user_api.route('/api/user/', methods=["DELETE"])
def delete_user():
    id = request.args.get('id')
    del_role = UserRole.delete().where(UserRole.c.user_id==id)
    db.session.execute(del_role)

    user = User.query.filter_by(id=id).first()
    user.query.delete()
    db.session.commit()
    
    return jsonify(user)

# TOOD: finish this function
@user_api.route('/api/user/', methods=["POST"])
def post_user():
    content = request.json
    return content

# TOOD: finish this function
@user_api.route('/api/user/', methods=["PATCH"])
def update_user():
    content = request.args.to_dict()
    update = User(**content)
    return jsonify(update)


@user_api.route('/api/selenium/', methods=["GET"])
def start_up():
    data = request.args.to_dict()
    return {'response': 'pong to user with id ' + data['user_id']}
