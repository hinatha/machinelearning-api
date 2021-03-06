"""empty message

Revision ID: 8f2b9309e1eb
Revises: db2b293056a0
Create Date: 2022-06-22 14:27:31.245431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f2b9309e1eb'
down_revision = 'db2b293056a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('file_id', sa.String(), nullable=True),
    sa.Column('filename', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image_info')
    # ### end Alembic commands ###
