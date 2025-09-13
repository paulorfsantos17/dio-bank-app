"""create uuid extension

Revision ID: d571965f0379
Revises: 
Create Date: 2025-09-13 14:28:05.730596

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'd571965f0379'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    import sqlalchemy as sa

    from alembic import op

    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')


def downgrade() -> None:
    import sqlalchemy as sa

    from alembic import op

    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp";')