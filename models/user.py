from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.user_todo import user_todo

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String())

    todos = relationship('Todo', secondary=user_todo, back_populates='users')

    def __init__(self, username) -> str:
        self.username = username
