import sqlalchemy as sa

from src.app.shared.database.database_config import metadata

user = sa.Table(
  'user',
  metadata,
  sa.Column('id', sa.UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
  sa.Column('name', sa.String(255)),
  sa.Column('email', sa.String(255)),
  sa.Column('password_hash', sa.String(255)),
  sa.Column('cpf', sa.String(14), nullable=False),
  sa.Column('created_at', sa.DateTime, nullable=False)
)