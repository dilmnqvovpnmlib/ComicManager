import json
from flask import Blueprint, jsonify, make_response, request
from api.models.models import Author, Comic, AuthorSchema, ComicSchema

# ルーティング設定
models_router = Blueprint('models_router', __name__)

@models_router.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.get_authors()
    author_schema = AuthorSchema(many=True)

    return make_response(jsonify({
        'code': 200,
        'users': author_schema.dump(authors)
    }))

@models_router.route('/comics', methods=['GET'])
def get_comics():
    comics = Comic.get_comics()
    comic_schema = ComicSchema(many=True)

    return make_response(jsonify({
        'code': 200,
        'users': comic_schema.dump(comics)
    }))

# @author_router.route('/users', methods=['POST'])
# def registUser():
#     # jsonデータを取得する
#     jsonData = json.dumps(request.json)
#     userData = json.loads(jsonData)

#     user = User.registUser(userData)
#     user_schema = UserSchema(many=True)

#     return make_response(jsonify({
#         'code': 200,
#         'user': user
#     }))
