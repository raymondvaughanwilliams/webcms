"""empty message

Revision ID: 1865173030f9
Revises: a76e2b056848
Create Date: 2023-01-07 10:11:41.617266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1865173030f9'
down_revision = 'a76e2b056848'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blocks', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_blocks_appearance_id_appearances'), 'appearances', ['appearance_id'], ['id'])

    with op.batch_alter_table('price', schema=None) as batch_op:
        batch_op.add_column(sa.Column('discount', sa.String(length=64), nullable=True))

    with op.batch_alter_table('web_feature', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mainpage', sa.String(length=10), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('web_feature', schema=None) as batch_op:
        batch_op.drop_column('mainpage')

    with op.batch_alter_table('price', schema=None) as batch_op:
        batch_op.drop_column('discount')

    with op.batch_alter_table('blocks', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_blocks_appearance_id_appearances'), type_='foreignkey')

    # ### end Alembic commands ###
