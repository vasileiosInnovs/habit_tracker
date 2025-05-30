"""Set email not null

Revision ID: 4e7a8b1b68e8
Revises: 8c006f31df47
Create Date: 2025-05-30 09:38:58.942911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e7a8b1b68e8'
down_revision: Union[str, None] = '8c006f31df47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column(
            'email',
            existing_type=sa.String(length=55),
            nullable=False
        )

def downgrade():
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column(
            'email',
            existing_type=sa.String(length=55),
            nullable=True
        )
