"""create posts tables

Revision ID: 596636e64780
Revises: 
Create Date: 2023-05-27 01:29:48.490488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '596636e64780'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
