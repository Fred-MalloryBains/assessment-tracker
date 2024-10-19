"""Create assessments table

Revision ID: 800e154a4a2e
Revises: 
Create Date: 2024-10-14 23:51:06.557138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '800e154a4a2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assessments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('moduleCode', sa.Integer(), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('assessments', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_assessments_title'), ['title'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assessments', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_assessments_title'))

    op.drop_table('assessments')
    # ### end Alembic commands ###
