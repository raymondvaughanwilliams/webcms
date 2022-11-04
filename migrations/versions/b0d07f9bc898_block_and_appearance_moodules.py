"""block and appearance moodules

Revision ID: b0d07f9bc898
Revises: 91198095914a
Create Date: 2021-12-24 01:03:35.103196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0d07f9bc898'
down_revision = '91198095914a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appearances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title_color', sa.String(length=64), nullable=True),
    sa.Column('subtitle_color', sa.String(length=64), nullable=True),
    sa.Column('paragraph_color', sa.String(length=64), nullable=True),
    sa.Column('title_font', sa.String(length=64), nullable=True),
    sa.Column('subtitle_font', sa.String(length=64), nullable=True),
    sa.Column('paragraph_font', sa.String(length=64), nullable=True),
    sa.Column('title_size', sa.Integer(), nullable=True),
    sa.Column('subtitle_size', sa.Integer(), nullable=True),
    sa.Column('paragraph_size', sa.Integer(), nullable=True),
    sa.Column('bootstrap_class1', sa.String(length=64), nullable=True),
    sa.Column('bootstrap_class2', sa.String(length=64), nullable=True),
    sa.Column('bootstrap_class3', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('appearance')
    op.add_column('blocks', sa.Column('appearance_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blocks', 'appearances', ['appearance_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blocks', type_='foreignkey')
    op.drop_column('blocks', 'appearance_id')
    op.create_table('appearance',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('block_id', sa.INTEGER(), nullable=False),
    sa.Column('title_color', sa.VARCHAR(length=64), nullable=True),
    sa.Column('subtitle_color', sa.VARCHAR(length=64), nullable=True),
    sa.Column('paragraph_color', sa.VARCHAR(length=64), nullable=True),
    sa.Column('title_font', sa.VARCHAR(length=64), nullable=True),
    sa.Column('subtitle_font', sa.VARCHAR(length=64), nullable=True),
    sa.Column('paragraph_font', sa.VARCHAR(length=64), nullable=True),
    sa.Column('title_size', sa.INTEGER(), nullable=True),
    sa.Column('subtitle_size', sa.INTEGER(), nullable=True),
    sa.Column('paragraph_size', sa.INTEGER(), nullable=True),
    sa.Column('bootstrap_class1', sa.VARCHAR(length=64), nullable=True),
    sa.Column('bootstrap_class2', sa.VARCHAR(length=64), nullable=True),
    sa.Column('bootstrap_class3', sa.VARCHAR(length=64), nullable=True),
    sa.ForeignKeyConstraint(['block_id'], ['blocks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('appearances')
    # ### end Alembic commands ###
