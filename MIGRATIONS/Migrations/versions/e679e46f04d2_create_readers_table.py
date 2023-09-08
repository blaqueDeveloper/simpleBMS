"""Create readers table

Revision ID: e679e46f04d2
Revises: 4e965c05ebbe
Create Date: 2023-09-07 16:39:04.905733

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e679e46f04d2'
down_revision: Union[str, None] = '4e965c05ebbe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('comments', sa.Column('reader_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('reader_name', sa.String(length=255), nullable=True))
    op.drop_column('comments', 'timestamp')
    op.create_table(
        'readers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False)
    )

def downgrade():
    op.drop_table('readers')
    op.drop_column('comments', 'reader_id')
    op.drop_column('comments', 'reader_name')
