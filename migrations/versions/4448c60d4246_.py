"""empty message

Revision ID: 4448c60d4246
Revises: f1249108d386
Create Date: 2021-06-25 07:27:20.533119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4448c60d4246'
down_revision = 'f1249108d386'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
