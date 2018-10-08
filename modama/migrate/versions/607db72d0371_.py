"""empty message

Revision ID: 607db72d0371
Revises: 37c46382b946
Create Date: 2018-10-07 18:51:56.829593

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
import flask_appbuilder


# revision identifiers, used by Alembic.
revision = '607db72d0371'
down_revision = '37c46382b946'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pawikan_stranding', sa.Column('encounter_id', sa.Integer(), nullable=False))
    op.drop_constraint('pawikan_stranding_observation_id_fkey', 'pawikan_stranding', type_='foreignkey')
    op.create_foreign_key(None, 'pawikan_stranding', 'pawikan_encounter', ['encounter_id'], ['id'])
    op.drop_column('pawikan_stranding', 'observation_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pawikan_stranding', sa.Column('observation_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'pawikan_stranding', type_='foreignkey')
    op.create_foreign_key('pawikan_stranding_observation_id_fkey', 'pawikan_stranding', 'pawikan_encounter', ['observation_id'], ['id'])
    op.drop_column('pawikan_stranding', 'encounter_id')
    # ### end Alembic commands ###