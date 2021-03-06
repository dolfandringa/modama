"""empty message

Revision ID: ca615d6f4a8c
Revises: 2094d7d7b54d
Create Date: 2018-10-14 10:45:28.759526

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
import flask_appbuilder


# revision identifiers, used by Alembic.
revision = 'ca615d6f4a8c'
down_revision = '2094d7d7b54d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pawikan_in_water', 'detailed_location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pawikan_in_water', sa.Column('detailed_location', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
