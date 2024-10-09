"""empty message

Revision ID: d032a9a0a90c
Revises: 
Create Date: 2024-07-11 00:22:37.074138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd032a9a0a90c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mini_links',
    sa.Column('url_address', sa.String(length=2048), nullable=False),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('public_key', sa.String(length=36), nullable=False),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('modified_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_key'),
    sa.UniqueConstraint('url_address')
    )
    op.create_table('mini_alias_links',
    sa.Column('alias_link', sa.String(length=2048), nullable=False),
    sa.Column('link_id', sa.INTEGER(), nullable=False),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('public_key', sa.String(length=36), nullable=False),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('modified_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['link_id'], ['mini_links.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias_link'),
    sa.UniqueConstraint('public_key')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mini_alias_links')
    op.drop_table('mini_links')
    # ### end Alembic commands ###