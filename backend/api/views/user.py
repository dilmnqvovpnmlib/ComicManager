import json

from flask import Blueprint, jsonify, make_response, request

from api.models import User, UserSchema

# ルーティング設定
user_router = Blueprint('user_router', __name__)

@user_router.route('/users', methods=['GET'])
def getUserList():
    users = User.getUserList()
    user_schema = UserSchema(many=True)
    print(user_schema.dump(users))

    return make_response(jsonify({
        'code': 200,
        'users': user_schema.dump(users)
    }))

@user_router.route('/users', methods=['POST'])
def registUser():
    # jsonデータを取得する
    jsonData = json.dumps(request.json)
    userData = json.loads(jsonData)

    user = User.registUser(userData)
    user_schema = UserSchema(many=True)

    return make_response(jsonify({
        'code': 200,
        'user': user
    }))
