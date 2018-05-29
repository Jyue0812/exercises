"""empty message

Revision ID: e43c017c3ea5
Revises: eb01a0194cbc
Create Date: 2018-05-29 17:03:55.464091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e43c017c3ea5'
down_revision = 'eb01a0194cbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('confirmed', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
