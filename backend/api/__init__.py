from flask import Flask, jsonify, make_response
from flask_cors import CORS

import config
from api.database import db

from .views.user import user_router


def create_app():

  app = Flask(__name__)

  # CORS対応
  CORS(app)

  # DB設定を読み込む
  app.config.from_object('config.Config')
  db.init_app(app)

  app.register_blueprint(user_router, url_prefix='/api')

  return app

app = create_app()
