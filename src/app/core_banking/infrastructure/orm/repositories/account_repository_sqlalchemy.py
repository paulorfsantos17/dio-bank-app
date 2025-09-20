
from app.core_banking.domain.value_objects.money import Money
from app.core_banking.infrastructure.orm.repositories.mappers.accounts_mappers import (
    AccountMapper,
)
from app.shared.domain.objects_values.unique_entity_id import UniqueEntityId
from src.app.core_banking.domain.entities.account import Account
from src.app.core_banking.domain.repositories.account_repository import (
    AccountRepository,
)
from src.app.core_banking.infrastructure.orm.models.account import account_model
from src.app.shared.database.database_config import database


class AccountRepositorySQLAlchemy(AccountRepository):
  async def save(self, account):
    record = AccountMapper.to_record(account)
    await database.execute(account_model.insert().values(**record))
    return account

  
  async def find_by_id(self, id):
    row = await database.fetch_one(account_model.select().where(account_model.c.id == id))
    if row is None:
      return None
    return AccountMapper.from_record(row)
  async def find_by_customer_id(self, id):
    row = await database.fetch_one(account_model.select().where(account_model.c.customer_id == id))
    if row is None:
      return None
    return AccountMapper.from_record(row)
    