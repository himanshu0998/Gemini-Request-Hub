# database.py
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from config import Config
import pymysql

db = Config()

MYSQL_USER = db.MYSQL_USER
MYSQL_HOST = db.MYSQL_HOST
MYSQL_PWD = db.MYSQL_PASSWORD
MYSQL_DBNAME = db.MYSQL_DB

DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}/{MYSQL_DBNAME}'
# print(DATABASE_URI)
engine = create_engine(DATABASE_URI, echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = scoped_session(session_factory)

Base = declarative_base()