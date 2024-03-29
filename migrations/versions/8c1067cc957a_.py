"""empty message

Revision ID: 8c1067cc957a
Revises: f78dab1201e8
Create Date: 2019-08-16 23:30:08.830793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c1067cc957a'
down_revision = 'f78dab1201e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer_key')
    op.drop_table('questions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('question', sa.VARCHAR(length=1200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('question')
    )
    op.create_table('answer_key',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('answer', sa.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
