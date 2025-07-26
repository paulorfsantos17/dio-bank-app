from src.app.auth.domain.entities.user import User
from src.app.auth.domain.repositories.user_repository import UserRepository
from src.app.auth.infrastructure.orm.models.user import user as user_model
from src.app.shared.database.database_config import database


class UserRepositorySqlAlchemy(UserRepository):
  async def save(self, user: User):
    query = user_model.insert().values(
        id=user.id,
        name=user.name,
        email=user.email,
        password_hash=user.password_hash,
        cpf=user.cpf,
        created_at=user.created_at
    )
    await database.execute(query)
    

  async def find_by_id(self, id):
      query = user_model.select().where(user_model.c.id == id)
      row = await database.fetch_one(query)
      if row is None:
          return None
      return User(
          id=row.id,
          name=row.name,
          email=row.email,
          password_hash=row.password_hash,
          cpf=row.cpf,
          created_at=row.created_at,
      )
  
  async def find_by_cpf(self, cpf):
      query = user_model.select().where(user_model.c.cpf == cpf)
      row = await database.fetch_one(query)
      if row is None:
          return None
      return User(
          id=row.id,
          name=row.name,
          email=row.email,
          password_hash=row.password_hash,
          cpf=row.cpf,
          created_at=row.created_at,
      )