"""add users avartar_url

Revision ID: 5154e0f5ea4f
Revises: da06bac9f26e
Create Date: 2026-11-12 11:40:11.837779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5154e0f5ea4f'
down_revision: Union[str, Sequence[str], None] = 'da06bac9f26e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
