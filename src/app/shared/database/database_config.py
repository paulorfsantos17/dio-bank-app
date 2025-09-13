# src/app/shared/database/database_config.py
import databases
import sqlalchemy
from sqlalchemy.orm import declarative_base

from src.app.shared.config.settings import settings

# Database async
database = databases.Database(settings.database_url)

# Metadata SQLAlchemy
metadata = sqlalchemy.MetaData()

# Engine padrão (sincrono) para criar tabelas
engine = sqlalchemy.create_engine(settings.database_url)

# Declarative Base para ORM
Base = declarative_base(metadata=metadata)