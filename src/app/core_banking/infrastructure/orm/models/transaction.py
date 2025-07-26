import sqlalchemy as sa

from src.app.shared.database.database_config import metadata

transaction_model = sa.Table(
  'transaction',
  metadata,
  sa.Column('id', sa.UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
  sa.Column('amount', sa.Float, nullable=False),
  sa.Column('account_from', sa.UUID(as_uuid=True), nullable=False),
  sa.Column('account_to', sa.UUID(as_uuid=True), nullable=False),
  sa.Column('created_at', sa.DateTime, nullable=False),
  sa.Column('timestamp', sa.DateTime, nullable=False)
)