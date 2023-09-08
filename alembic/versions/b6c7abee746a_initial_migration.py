"""initial migration

Revision ID: b6c7abee746a
Revises: 
Create Date: 2023-09-07 09:49:03.774122

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6c7abee746a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'todos',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('task', sa.String(255), nullable=False),
        sa.Column('category', sa.String(255)),
        sa.Column('date_added', sa.DateTime, server_default=sa.func.now()),
        sa.Column('date_completed', sa.DateTime),
        sa.Column('status', sa.Integer, default=0),
        sa.Column('position', sa.Integer),
    )


def downgrade() -> None:
    op.drop_table('todos')
