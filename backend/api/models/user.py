from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

import sqlalchemy
import os
from os.path import join, dirname
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_USER = os.environ.get('DB_USER')
print(DB_USER)
DB_PASSWORD = os.environ.get('DB_PASSWORD')

url = f'mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@localhost/comic?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ma = Marshmallow(app)
db = SQLAlchemy(app)

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    # address= db.Column(db.String(100), nullable=True)
    # tel = db.Column(db.String(20), nullable=True)
    
    # mail = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.name

    def getUserList():

        # select * from users
        user_list = db.session.query(User).all()
        print(user_list, 'user_list')

        if user_list == None:
          return []
        else:
          return user_list

    def registUser(user):
      record = User(
        name = user['name'],
        # address = user['address'],
        # tel = user['tel'],
        # mail = user['mail']
      )
    
      # insert into users(name, address, tel, mail) values(...)
      db.session.add(record)
      db.session.commit()

      return user

class UserSchema(ma.ModelSchema):
    class Meta:
      model = User
      fields = ('id', 'name',) # ('id', 'name', 'address', 'tel', 'mail')


if __name__ == '__main__':
    manager.run()