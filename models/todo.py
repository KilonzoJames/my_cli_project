from typing import List
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models.base import Base
from models.user_todo import user_todo
from models.user import User

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String, nullable=False)
    category = Column(String)
    date_added = Column(DateTime(timezone=True), server_default=func.now())
    date_completed = Column(DateTime(timezone=True))
    status = Column(Integer, default=0)
    position = Column(Integer)

    users = relationship('User', secondary=user_todo, back_populates='todos')


    def __init__(self, task, category,
                 date_added=None, date_completed=None,
                 status=None, position=None, max_size=None):
        self.task = task
        self.category = category
        self.date_added = date_added
        self.date_completed = date_completed
        self.status = status # 1 = open, 2 = completed
        self.position = position
        self.todos: List[str] = []
        self.max_size = max_size
    def __repr__(self) -> str:
        return f"({self.task}, {self.category}, {self.date_added}, {self.date_completed}, {self.status}, {self.position})"
    def add(self, todo):
        if self.size() == self.max_size:
            raise OverflowError("Cannot add more todos, the list is full")
        self.todos.append(todo)
    def size(self):
        return len(self.todos)
    def get_todos(self):
        return self.todos
    