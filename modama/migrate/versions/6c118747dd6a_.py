"""empty message

Revision ID: 6c118747dd6a
Revises: 4aebd26bcae1
Create Date: 2018-10-11 11:08:28.586169

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
import flask_appbuilder


# revision identifiers, used by Alembic.
revision = '6c118747dd6a'
down_revision = '4aebd26bcae1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pawikan_encounter_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pawikan_facility_encountered',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_fishing_gear',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_fishing_turtle_condition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_fishing_turtle_disposition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_general_version',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('encounter_type_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('alive', sa.Enum('yes', 'no', name='pawikanyesnoenum'), autoincrement=False, nullable=True),
    sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326), autoincrement=False, nullable=True),
    sa.Column('location_type_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('barangay_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('species_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('lateral_scutes', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('prefrontal_scutes', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('incident_description', sa.Text(), autoincrement=False, nullable=True),
    sa.Column('sex_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('curved_carapace_length', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('origin_of_report', sa.Text(), autoincrement=False, nullable=True),
    sa.Column('report_generator', sa.Text(), autoincrement=False, nullable=True),
    sa.Column('tagged', sa.Enum('yes', 'no', name='pawikanyesnoenum'), autoincrement=False, nullable=True),
    sa.Column('outcome_id', sa.Integer(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'transaction_id')
    )
    op.create_index(op.f('ix_pawikan_general_version_end_transaction_id'), 'pawikan_general_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_pawikan_general_version_operation_type'), 'pawikan_general_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_pawikan_general_version_transaction_id'), 'pawikan_general_version', ['transaction_id'], unique=False)
    op.create_table('pawikan_hatchling_disposition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_hatchling_location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_inwater_activity_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_inwater_turtle_activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_inwater_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_location_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_nest_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_nesting_action_taken',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_outcome',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pawikan_species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genus', sa.String(length=255), nullable=False),
    sa.Column('species', sa.String(length=255), nullable=False),
    sa.Column('common_name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('picture', flask_appbuilder.models.mixins.ImageColumn(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('genus', 'species', name='scientific_name_uc')
    )
    op.create_table('pawikan_stranding_cause',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pawikan_stranding_turtle_disposition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pawikan_trade_exhibit_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_trade_turtle_condition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_trade_turtle_disposition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transaction',
    sa.Column('issued_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('remote_addr', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_general',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('encounter_type_id', sa.Integer(), nullable=False),
    sa.Column('alive', sa.Enum('yes', 'no', name='pawikanyesnoenum'), nullable=False),
    sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326), nullable=True),
    sa.Column('location_type_id', sa.Integer(), nullable=False),
    sa.Column('barangay_id', sa.Integer(), nullable=False),
    sa.Column('species_id', sa.Integer(), nullable=False),
    sa.Column('lateral_scutes', sa.Integer(), nullable=False),
    sa.Column('prefrontal_scutes', sa.Integer(), nullable=False),
    sa.Column('incident_description', sa.Text(), nullable=True),
    sa.Column('sex_id', sa.Integer(), nullable=True),
    sa.Column('curved_carapace_length', sa.Integer(), nullable=True),
    sa.Column('origin_of_report', sa.Text(), nullable=True),
    sa.Column('report_generator', sa.Text(), nullable=True),
    sa.Column('tagged', sa.Enum('yes', 'no', name='pawikanyesnoenum'), nullable=False),
    sa.Column('outcome_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['barangay_id'], ['barangay.id'], ),
    sa.ForeignKeyConstraint(['encounter_type_id'], ['pawikan_encounter_type.id'], ),
    sa.ForeignKeyConstraint(['id'], ['base_observation.id'], ),
    sa.ForeignKeyConstraint(['location_type_id'], ['pawikan_location_type.id'], ),
    sa.ForeignKeyConstraint(['outcome_id'], ['pawikan_outcome.id'], ),
    sa.ForeignKeyConstraint(['sex_id'], ['sex.id'], ),
    sa.ForeignKeyConstraint(['species_id'], ['pawikan_species.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_fisheries_interaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('general_id', sa.Integer(), nullable=False),
    sa.Column('fisher_details', sa.Text(), nullable=True),
    sa.Column('vessel_details', sa.Integer(), nullable=True),
    sa.Column('fishing_gear_id', sa.Integer(), nullable=True),
    sa.Column('turtle_condition_id', sa.Integer(), nullable=False),
    sa.Column('turtle_disposition_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fishing_gear_id'], ['pawikan_fishing_gear.id'], ),
    sa.ForeignKeyConstraint(['general_id'], ['pawikan_general.id'], ),
    sa.ForeignKeyConstraint(['turtle_condition_id'], ['pawikan_fishing_turtle_condition.id'], ),
    sa.ForeignKeyConstraint(['turtle_disposition_id'], ['pawikan_fishing_turtle_disposition.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_general_picture',
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('changed_on', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture', flask_appbuilder.models.mixins.ImageColumn(), nullable=True),
    sa.Column('general_id', sa.Integer(), nullable=False),
    sa.Column('created_by_fk', sa.Integer(), nullable=False),
    sa.Column('changed_by_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['general_id'], ['pawikan_general.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_hatchlings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('general_id', sa.Integer(), nullable=False),
    sa.Column('hatchery_nest', sa.Enum('yes', 'no', name='pawikanyesnoenum'), nullable=False),
    sa.Column('location_of_hatchlings_id', sa.Integer(), nullable=False),
    sa.Column('datetime_first_emergence', sa.DateTime(timezone=True), nullable=True),
    sa.Column('datetime_last_emergence', sa.DateTime(timezone=True), nullable=True),
    sa.Column('carapace_color', sa.Enum('black', 'white', name='pawikanblackwhiteenum'), nullable=False),
    sa.Column('p_color', sa.Enum('black', 'white', name='pawikanblackwhiteenum'), nullable=False),
    sa.Column('hatchling_disposition_id', sa.Integer(), nullable=False),
    sa.Column('released', sa.Enum('yes', 'no', name='pawikanyesnoenum'), nullable=False),
    sa.ForeignKeyConstraint(['general_id'], ['pawikan_general.id'], ),
    sa.ForeignKeyConstraint(['hatchling_disposition_id'], ['pawikan_hatchling_disposition.id'], ),
    sa.ForeignKeyConstraint(['location_of_hatchlings_id'], ['pawikan_hatchling_location.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_in_water',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('general_id', sa.Integer(), nullable=False),
    sa.Column('inwater_encounter_type_id', sa.Integer(), nullable=False),
    sa.Column('your_activity_id', sa.Integer(), nullable=False),
    sa.Column('detailed_location', sa.Text(), nullable=True),
    sa.Column('depth', sa.Integer(), nullable=True),
    sa.Column('turtle_activity_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['general_id'], ['pawikan_general.id'], ),
    sa.ForeignKeyConstraint(['inwater_encounter_type_id'], ['pawikan_inwater_type.id'], ),
    sa.ForeignKeyConstraint(['turtle_activity_id'], ['pawikan_inwater_turtle_activity.id'], ),
    sa.ForeignKeyConstraint(['your_activity_id'], ['pawikan_inwater_activity_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_nest_evaluation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('general_id', sa.Integer(), nullable=False),
    sa.Column('number_of_eggs_known', sa.Enum('yes', 'no', name='pawikanyesnoenum'), nullable=False),
    sa.Column('nest_id', sa.String(), nullable=True),
    sa.Column('num_eggs_s', sa.Integer(), nullable=True),
    sa.Column('num_eggs_uht', sa.Integer(), nullable=True),
    sa.Column('num_eggs_uh', sa.Integer(), nullable=True),
    sa.Column('num_eggs_lpe', sa.Integer(), nullable=True),
    sa.Column('num_eggs_dpe', sa.Integer(), nullable=True),
    sa.Column('num_eggs_ud', sa.Integer(), nullable=True),
    sa.Column('num_eggs_p', sa.Integer(), nullable=True),
    sa.Column('num_eggs_din', sa.Integer(), nullable=True),
    sa.Column('num_eggs_lin', sa.Integer(), nullable=True),
    sa.Column('num_emerged', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['general_id'], ['pawikan_general.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_nest_with_egg',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('general_id', sa.Integer(), nullable=False),
    sa.Column('nest_type_id', sa.Integer(), nullable=False),
    sa.Column('barangay_id', sa.Integer(), nullable=False),
    sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326), nullable=True),
    sa.Column('detailed_location', sa.Text(), nullable=True),
    sa.Column('nest_id', sa.String(), nullable=True),
    sa.Column('action_taken_id', sa.Integer(), nullable=True),
    sa.Column('area_secure', sa.Enum('yes', 'no', name='pawikanyesnoenum'), nullable=True),
    sa.ForeignKeyConstraint(['action_taken_id'], ['pawikan_nesting_action_taken.id'], ),
    sa.ForeignKeyConstraint(['barangay_id'], ['barangay.id'], ),
    sa.ForeignKeyConstraint(['general_id'], ['pawikan_general.id'], ),
    sa.ForeignKeyConstraint(['nest_type_id'], ['pawikan_nest_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_stranding',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('general_id', sa.Integer(), nullable=False),
    sa.Column('stranding_code', sa.Enum('code1', 'code2', 'code3', 'code4', 'code5', 'code6', 'code7', name='pawikanstrandingcodeenum'), nullable=False),
    sa.Column('turtle_disposition_id', sa.Integer(), nullable=False),
    sa.Column('suspected_cause_id', sa.Integer(), nullable=False),
    sa.Column('confirmed_cause', sa.Text(), nullable=True),
    sa.Column('cause_confirmed_by', sa.Text(), nullable=True),
    sa.Column('sample_collected', sa.Enum('yes', 'no', name='pawikanyesnoenum'), nullable=False),
    sa.Column('necropsy_conducted', sa.Enum('yes', 'no', name='pawikanyesnoenum'), nullable=False),
    sa.Column('necropsy_carried_out_by', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['general_id'], ['pawikan_general.id'], ),
    sa.ForeignKeyConstraint(['suspected_cause_id'], ['pawikan_stranding_cause.id'], ),
    sa.ForeignKeyConstraint(['turtle_disposition_id'], ['pawikan_stranding_turtle_disposition.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_tagging',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('general_id', sa.Integer(), nullable=False),
    sa.Column('existing_tags_origin', sa.Enum('foreign', 'philippine', name='pawikantagoriginenum'), nullable=False),
    sa.Column('existing_tags_left', sa.Text(), nullable=True),
    sa.Column('existing_tags_right', sa.Text(), nullable=True),
    sa.Column('new_tags_left', sa.Text(), nullable=True),
    sa.Column('new_tags_right', sa.Text(), nullable=True),
    sa.Column('replacement_tags_left', sa.Text(), nullable=True),
    sa.Column('replacement_tags_right', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['general_id'], ['pawikan_general.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pawikan_trade_exhibit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('general_id', sa.Integer(), nullable=False),
    sa.Column('trade_exhibit_type_id', sa.Integer(), nullable=False),
    sa.Column('facility_encountered_id', sa.Integer(), nullable=False),
    sa.Column('turtle_condition_id', sa.Integer(), nullable=False),
    sa.Column('amount_encountered', sa.Integer(), nullable=True),
    sa.Column('unit_amount_encountered', sa.Enum('kgs', 'pieces', name='pawikantradeunitenum'), nullable=True),
    sa.Column('turtle_disposition_id', sa.Integer(), nullable=True),
    sa.Column('facility_address', sa.Text(), nullable=True),
    sa.Column('facility_contact_person', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['facility_encountered_id'], ['pawikan_facility_encountered.id'], ),
    sa.ForeignKeyConstraint(['general_id'], ['pawikan_general.id'], ),
    sa.ForeignKeyConstraint(['trade_exhibit_type_id'], ['pawikan_trade_exhibit_type.id'], ),
    sa.ForeignKeyConstraint(['turtle_condition_id'], ['pawikan_trade_turtle_condition.id'], ),
    sa.ForeignKeyConstraint(['turtle_disposition_id'], ['pawikan_trade_turtle_disposition.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pawikan_trade_exhibit')
    op.drop_table('pawikan_tagging')
    op.drop_table('pawikan_stranding')
    op.drop_table('pawikan_nest_with_egg')
    op.drop_table('pawikan_nest_evaluation')
    op.drop_table('pawikan_in_water')
    op.drop_table('pawikan_hatchlings')
    op.drop_table('pawikan_general_picture')
    op.drop_table('pawikan_fisheries_interaction')
    op.drop_table('pawikan_general')
    op.drop_table('transaction')
    op.drop_table('pawikan_trade_turtle_disposition')
    op.drop_table('pawikan_trade_turtle_condition')
    op.drop_table('pawikan_trade_exhibit_type')
    op.drop_table('pawikan_stranding_turtle_disposition')
    op.drop_table('pawikan_stranding_cause')
    op.drop_table('pawikan_species')
    op.drop_table('pawikan_outcome')
    op.drop_table('pawikan_nesting_action_taken')
    op.drop_table('pawikan_nest_type')
    op.drop_table('pawikan_location_type')
    op.drop_table('pawikan_inwater_type')
    op.drop_table('pawikan_inwater_turtle_activity')
    op.drop_table('pawikan_inwater_activity_type')
    op.drop_table('pawikan_hatchling_location')
    op.drop_table('pawikan_hatchling_disposition')
    op.drop_index(op.f('ix_pawikan_general_version_transaction_id'), table_name='pawikan_general_version')
    op.drop_index(op.f('ix_pawikan_general_version_operation_type'), table_name='pawikan_general_version')
    op.drop_index(op.f('ix_pawikan_general_version_end_transaction_id'), table_name='pawikan_general_version')
    op.drop_table('pawikan_general_version')
    op.drop_table('pawikan_fishing_turtle_disposition')
    op.drop_table('pawikan_fishing_turtle_condition')
    op.drop_table('pawikan_fishing_gear')
    op.drop_table('pawikan_facility_encountered')
    op.drop_table('pawikan_encounter_type')
    # ### end Alembic commands ###