"""create dietitian table

Revision ID: e9a452625402
Revises: 2394eb8be9d3
Create Date: 2024-10-02 18:13:55.255130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'e9a452625402'
down_revision: Union[str, None] = '2394eb8be9d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dietitian',
    sa.Column('dietitian_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.String(length=255), nullable=False),
    sa.Column('email', sqlmodel.String(length=255), nullable=False),
    sa.Column('qualification', sqlmodel.String(length=255), nullable=False),
    sa.Column('experience_years', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('dietitian_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dietitian')
    # ### end Alembic commands ###
