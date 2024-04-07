"""
A module for configuring and initializing the database connection using SQLAlchemy and MySQL.

This module defines the database URI based on configurations specified in a separate `config.py` module. It utilizes SQLAlchemy for ORM (Object-Relational Mapping) capabilities and `pymysql` as the database driver to connect to a MySQL database. The connection details such as the database username, host, password, and database name are retrieved from the `Config` object, which is expected to be defined in the `config.py` module.

Upon importing this module and if the specified database does not exist, it will automatically create the database. It sets up a `SessionLocal` class that can be used to create session instances for interacting with the database. The `Base` class from SQLAlchemy's declarative base is also instantiated, which can be used as a base class for model definitions.

Functions and Attributes:
- `DATABASE_URI`: A string representing the fully constructed database URI.
- `engine`: The SQLAlchemy engine instance connected to the database.
- `SessionLocal`: A scoped session factory for creating new database session objects.
- `Base`: The base class for declarative class definitions.

Usage:
Import `SessionLocal` to create new database sessions and `Base` to define ORM models in separate modules.
"""

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