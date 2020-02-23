import sqlalchemy
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

url = f'mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@localhost/comic?charset=utf8'

engine = sqlalchemy.create_engine(url, echo=True)

engine.execute(f'DROP TABLE IF EXISTS posts')

engine.execute('''
    CREATE TABLE posts (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        title CHAR(30),
        body TEXT
    )
''')