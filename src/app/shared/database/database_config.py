import databases
import sqlalchemy

from src.app.shared.config.settings import settings

database = databases.Database(settings.database_url)
metadata = sqlalchemy.MetaData()


engine = sqlalchemy.create_engine(
  settings.database_url
)