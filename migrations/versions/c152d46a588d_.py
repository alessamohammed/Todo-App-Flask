"""empty message

Revision ID: c152d46a588d
Revises: 43d956b390ac
Create Date: 2021-06-23 04:32:04.528074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c152d46a588d'
down_revision = '43d956b390ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    
    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')
    
    op.alter_column('todos', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
