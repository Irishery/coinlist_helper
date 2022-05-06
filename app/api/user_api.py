from flask import Blueprint, jsonify, request
import httpx
from app import db
from app.models import User, UserRole


user_api = Blueprint('user_api', __name__)
client = httpx.Client(timeout=None)


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


@user_api.route('/api/selenium/', methods=["GET"])
def start_up():
    data = request.args.to_dict()
    print(data)
    print('a')
    r = client.request(
            "get", "http://127.0.0.1:8181/worker/run",
            params=data,
            headers={'content-type': 'application/json'}
    )

    return {'responses': 'pong to user with id ' + data['user_id']}


@user_api.route('/api/selenium/', methods=["PATCH"])
def edit_row():
    data = request.args.to_dict()
    r = client.request(
        "get", "http://127.0.0.1:8181/worker/run/",
        params=data,
        headers={'content-type': 'application/json'}
    )
    return {'response': 'pong to user with id ' + data['user_id']}
