from crypt import methods
from flask import Blueprint, jsonify
from flask_restful import Resource
from app import db
from app.models import User


user_api = Blueprint('user_api', __name__)


class UserApi(Resource):
    def get(self, id):
        res = User.query.filter_by(id=id).first()
        return jsonify(res)

    def put(self, id):
        pass

    def delete(self, id):
        to_del = User.query.filter_by(id=id).first()
        db.session.delete(to_del)
        return jsonify(to_del)
