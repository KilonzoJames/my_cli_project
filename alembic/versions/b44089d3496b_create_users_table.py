"""Create users table

Revision ID: b44089d3496b
Revises: b6c7abee746a
Create Date: 2023-09-07 19:10:19.965794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b44089d3496b'
down_revision: Union[str, None] = 'b6c7abee746a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
     op.drop_table('users')
