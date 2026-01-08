"""Create address for user column

Revision ID: d7ddac73f88b
Revises: 65c4413e5e18
Create Date: 2026-01-07 10:11:36.510543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7ddac73f88b'
down_revision: Union[str, Sequence[str], None] = '65c4413e5e18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('address', sa.String(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
