"""add foreign key indexes

Revision ID: 68f717c836c3
Revises: 967e5c0ab97b
Create Date: 2026-10-07 22:45:00.968344

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68f717c836c3'
down_revision: Union[str, Sequence[str], None] = '967e5c0ab97b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_index(
        op.f('ix_rowdy_venue_configurations_venue_id'),
        'venue_configurations',
        ['venue_id'],
        unique=False,
        schema='rowdy',
    )
    op.create_index(
        op.f('ix_rowdy_events_organisation_id'),
        'events',
        ['organisation_id'],
        unique=False,
        schema='rowdy',
    )
    op.create_index(
        op.f('ix_rowdy_events_venue_id'),
        'events',
        ['venue_id'],
        unique=False,
        schema='rowdy',
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_rowdy_events_venue_id'), table_name='events', schema='rowdy')
    op.drop_index(op.f('ix_rowdy_events_organisation_id'), table_name='events', schema='rowdy')
    op.drop_index(
        op.f('ix_rowdy_venue_configurations_venue_id'),
        table_name='venue_configurations',
        schema='rowdy',
    )
