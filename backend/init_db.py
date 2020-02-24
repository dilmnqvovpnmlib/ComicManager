import os
from os.path import dirname, join
import sqlalchemy
from dotenv import load_dotenv
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from api.models.models import Author, Comic

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

url = f'mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@localhost/comic?charset=utf8'
engine = sqlalchemy.create_engine(url, echo=True)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

ma = Marshmallow(app)
db = SQLAlchemy(app)

# comic_datas = [
#     {'author_id': 1, 'name': "BLOODY MONDAY"},
#     {'author_id': 1, 'name': "金田一少年の事件簿"},
#     {'author_id': 2, 'name': "ブルーロック"},
#     {'author_id': 3, 'name': "左ききのエレン"},
#     {'author_id': 4, 'name': "ブルーピリオド"},
#     {'author_id': 5, 'name': "ランウェイで笑って"},
#     {'author_id': 6, 'name': "約束のネバーランド"},
#     {'author_id': 7, 'name': "憂国のモリアーティ"},
#     {'author_id': 8, 'name': "進撃の巨人"},
#     {'author_id': 9, 'name': "HUNTER×HUNTER"},
# ]
# for comic_data in comic_datas:
#     comic = Comic(name=comic_data['name'], author_id=comic_data['author_id']) 
#     db.session.add(comic)
#     db.session.commit()

# author_datas = [
#     {'name': "龍門諒"},
#     {'name': "金城宗幸"},
#     {'name': "かっぴー"},
#     {'name': "山口つばさ"},
#     {'name': "猪ノ谷言葉"},
#     {'name': "白井カイウ"},
#     {'name': "竹内良輔"},
#     {'name': "諫山創"},
#     {'name': "冨樫義博"},
# ]
# for author_data in author_datas:
#     author = Author(name=author_data['name']) 
#     db.session.add(author)
#     db.session.commit()