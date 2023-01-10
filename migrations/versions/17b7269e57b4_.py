"""empty message

Revision ID: 17b7269e57b4
Revises: 1865173030f9
Create Date: 2023-01-07 12:40:38.656662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17b7269e57b4'
down_revision = '1865173030f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('web_feature', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image1', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('image2', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('image3', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('web_feature', schema=None) as batch_op:
        batch_op.drop_column('image3')
        batch_op.drop_column('image2')
        batch_op.drop_column('image1')

    # ### end Alembic commands ###