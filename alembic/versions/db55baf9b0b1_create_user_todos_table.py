"""Create user_todos table

Revision ID: db55baf9b0b1
Revises: b44089d3496b
Create Date: 2023-09-08 14:33:26.773889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db55baf9b0b1'
down_revision: Union[str, None] = 'b44089d3496b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_todos',
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), primary_key=True),
        sa.Column('todo_id', sa.Integer(), sa.ForeignKey('todos.id'), primary_key=True),
    )


def downgrade() -> None:
    op.drop_table('user_todos')
