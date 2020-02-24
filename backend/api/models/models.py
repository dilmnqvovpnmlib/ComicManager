import os
from os.path import dirname, join

import sqlalchemy
from dotenv import load_dotenv
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
url = f'mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@localhost/comic?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ma = Marshmallow(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)


class Comic(db.Model):
    __tablename__ = 'comics'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    desc = db.Column(db.Text, nullable=True)
    published_counts = db.Column(db.Integer, nullable=True)
    published_date = db.Column(db.Date, nullable=True)
    is_hidden = db.Column(db.Boolean, default=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    def get_comics():
        comics = db.session.query(Comic).all()
        return []  if comics == None else comics

    def post_comic(comic):
        record = Comic(
          name = comic['name'],
          desc = comic['desc'],
          published_counts = comic['published_counts'],
          published_date = comic['published_date'],
          is_hidden = comic['is_hidden'],
          author_id = comic['author_id'],
        )
        db.session.add(record)
        db.session.commit()
        return comic

    def __repr__(self):
        return '<Comic %r>' % self.name


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    belong_to = db.Column(db.String(255), nullable=True)
    birth_day = db.Column(db.Date, nullable=True)
    desc = db.Column(db.Text, nullable=True)
    is_hidden = db.Column(db.Boolean, default=False)
    comics = db.relationship('Comic', backref='author', lazy=True)

    def get_authors():
        authors = db.session.query(Author).all()
        print(authors)
        return []  if authors == None else authors

    def post_author(author):
        record = Author(
          name = author['name'],
          belong_to = author['belong_to'],
          birth_day = author['birth_day'],
          desc = author['desc'],
          is_hidden = author['is_hidden'],
        )
        db.session.add(record)
        db.session.commit()
        return author

    def __repr__(self):
        return '<Author %r>' % self.name


class ComicSchema(ma.ModelSchema):
    class Meta:
        model = Comic
        fields = (
            'id',
            'name',
            'desc',
            'published_counts',
            'published_date',
            'is_hidden',
            'author_id',
        )


class AuthorSchema(ma.ModelSchema):
    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'belong_to',
            'birth_day',
            'desc',
            'is_hidden',
        )


if __name__ == '__main__':
    manager.run()
