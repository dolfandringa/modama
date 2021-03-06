"""empty message

Revision ID: fa461dba216e
Revises: 93bb40148399
Create Date: 2018-10-13 16:05:30.239584

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
import flask_appbuilder


# revision identifiers, used by Alembic.
revision = 'fa461dba216e'
down_revision = '93bb40148399'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pawikan_general', sa.Column('detailed_location', sa.Text(), nullable=True))
    op.add_column('pawikan_general_version', sa.Column('detailed_location', sa.Text(), autoincrement=False, nullable=True))
    op.drop_column('pawikan_nest_with_egg', 'detailed_location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pawikan_nest_with_egg', sa.Column('detailed_location', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('pawikan_general_version', 'detailed_location')
    op.drop_column('pawikan_general', 'detailed_location')
    # ### end Alembic commands ###
