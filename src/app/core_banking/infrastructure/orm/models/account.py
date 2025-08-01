import sqlalchemy as sa

from src.app.shared.database.database_config import metadata

account_model = sa.Table(
  'account',
  metadata,
  sa.Column('id', sa.UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
  sa.Column('balance', sa.Float, nullable=False),
  sa.Column('created_at', sa.DateTime, nullable=False),
  sa.Column('status', sa.Boolean, nullable=False),
  sa.Column('customer_id', sa.UUID(as_uuid=True), nullable=False)
)
  