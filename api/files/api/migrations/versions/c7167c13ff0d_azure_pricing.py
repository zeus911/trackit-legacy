"""Azure pricing

Revision ID: c7167c13ff0d
Revises: cbae861a97fc
Create Date: 2016-06-24 08:45:27.725915

"""

# revision identifiers, used by Alembic.
revision = 'c7167c13ff0d'
down_revision = 'cbae861a97fc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('azure_pricing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('offer', sa.Unicode(length=63), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('region', sa.String(length=32), nullable=True),
    sa.Column('value', sa.BLOB(length=16000000), nullable=False),
    sa.PrimaryKeyConstraint('id', 'offer')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('azure_pricing')
    ### end Alembic commands ###