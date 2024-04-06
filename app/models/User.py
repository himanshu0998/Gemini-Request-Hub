# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    username = Column(String(50), primary_key=True, unique=True, nullable=False)
    password = Column(String(200), nullable=False)
