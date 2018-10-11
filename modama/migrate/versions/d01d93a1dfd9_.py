"""empty message

Revision ID: d01d93a1dfd9
Revises: 607db72d0371
Create Date: 2018-10-09 20:10:19.760644

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
import flask_appbuilder
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd01d93a1dfd9'
down_revision = '607db72d0371'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_pawikan_encounter_version_end_transaction_id', table_name='pawikan_encounter_version')
    op.drop_index('ix_pawikan_encounter_version_operation_type', table_name='pawikan_encounter_version')
    op.drop_index('ix_pawikan_encounter_version_transaction_id', table_name='pawikan_encounter_version')
    op.drop_table('pawikan_encounter_version')
    op.drop_table('pawikan_encounter_picture')
    op.drop_table('pawikan_stranding')
    op.drop_table('transaction')
    op.drop_table('pawikan_encounter')
    op.drop_table('pawikan_species')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pawikan_encounter',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('species_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ccl', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sex_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326), autoincrement=False, nullable=True),
    sa.Column('encounter_type', postgresql.ENUM('Stranding', 'Fisheries bycatch', 'Nesting', name='encounter_type'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id'], ['base_observation.id'], name='pawikan_encounter_id_fkey'),
    sa.ForeignKeyConstraint(['sex_id'], ['sex.id'], name='pawikan_encounter_sex_id_fkey'),
    sa.ForeignKeyConstraint(['species_id'], ['pawikan_species.id'], name='pawikan_encounter_species_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pawikan_encounter_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('pawikan_species',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('pawikan_species_id_seq'::regclass)"), nullable=False),
    sa.Column('genus', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('species', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('common_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('picture', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pawikan_species_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('transaction',
    sa.Column('issued_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('id', sa.BIGINT(), nullable=False),
    sa.Column('remote_addr', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='transaction_pkey')
    )
    op.create_table('pawikan_stranding',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('alive', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('encounter_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['encounter_id'], ['pawikan_encounter.id'], name='pawikan_stranding_encounter_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pawikan_stranding_pkey')
    )
    op.create_table('pawikan_encounter_picture',
    sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('changed_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('picture', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('encounter_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_by_fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('changed_by_fk', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], name='pawikan_encounter_picture_changed_by_fk_fkey'),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], name='pawikan_encounter_picture_created_by_fk_fkey'),
    sa.ForeignKeyConstraint(['encounter_id'], ['pawikan_encounter.id'], name='pawikan_encounter_picture_encounter_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='pawikan_encounter_picture_pkey')
    )
    op.create_table('pawikan_encounter_version',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('species_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ccl', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sex_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('operation_type', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('encounter_type', postgresql.ENUM('Stranding', 'Fisheries bycatch', 'Nesting', name='encounter_type'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', 'transaction_id', name='pawikan_encounter_version_pkey')
    )
    op.create_index('ix_pawikan_encounter_version_transaction_id', 'pawikan_encounter_version', ['transaction_id'], unique=False)
    op.create_index('ix_pawikan_encounter_version_operation_type', 'pawikan_encounter_version', ['operation_type'], unique=False)
    op.create_index('ix_pawikan_encounter_version_end_transaction_id', 'pawikan_encounter_version', ['end_transaction_id'], unique=False)
    # ### end Alembic commands ###
