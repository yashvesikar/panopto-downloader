"""api body logging

Revision ID: 76da712b9618
Revises: 121ff831ded3
Create Date: 2025-01-30 02:04:08.119866

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76da712b9618'
down_revision: Union[str, None] = '121ff831ded3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_request', sa.Column('body', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('api_request', 'body')
    # ### end Alembic commands ###
