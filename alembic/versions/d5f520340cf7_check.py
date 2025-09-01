"""check

Revision ID: d5f520340cf7
Revises: b4e57f2f613e
Create Date: 2025-09-01 15:32:06.297803

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5f520340cf7'
down_revision: Union[str, Sequence[str], None] = 'b4e57f2f613e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
