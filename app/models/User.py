"""
Defines the User model for the database using SQLAlchemy ORM.

This class represents the 'users' table in the database, with each instance corresponding to a row in the table. The User model includes two fields: 'username' and 'password'. The 'username' field serves as the primary key and is set to be unique and not nullable, ensuring that each user has a distinct username. The 'password' field stores the user's password and is also not nullable, indicating that a password must be provided for each user.

Attributes:
    __tablename__ (str): The name of the table in the database, set to 'users'.
    username (Column): A String column that stores the username. It is the primary key, unique, and not nullable.
    password (Column): A String column that stores the password. It is not nullable and can store up to 200 characters.

Usage:
    This class is intended to be used in conjunction with SQLAlchemy's ORM capabilities to facilitate interactions with the 'users' table in a database. Instances of the User class can be created, modified, queried, and deleted using SQLAlchemy session operations, allowing for straightforward management of user data within an application.
"""


from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    username = Column(String(50), primary_key=True, unique=True, nullable=False)
    emailid = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
