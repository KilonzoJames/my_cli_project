from sqlalchemy import Table, Column, ForeignKey
from models.base import Base

user_todo = Table(
    'user_todos',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('todo_id', ForeignKey('todos.id'), primary_key=True),
    extend_existing=True,
)
