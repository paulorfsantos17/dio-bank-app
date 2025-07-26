
from src.app.core_banking.domain.entities.account import Account
from src.app.core_banking.domain.repositories.account_repository import (
    AccountRepository,
)
from src.app.core_banking.infrastructure.orm.models.account import account_model
from src.app.shared.database.database_config import database


class AccountRepositorySQLAlchemy(AccountRepository):
  async def save(self, account):
    query = await    account_model.insert().values(
        id=account.id,
        balance=account.balance,
        created_at=account.created_at,
        status=account.status,
        customer_id=account.customer_id
        
        )
    
    await database.execute(query)
  
  async def find_by_id(self, id):
    query = account_model.select().where(account_model.c.id == id)
    row = await database.fetch_one(query)
    if row is None:
        return None
    return Account(
        id=row.id,
        balance=row.balance,
        created_at=row.created_at,
        status=row.status,
        customer_id=row.customer_id
    )
    
  async def find_by_customer_id(self, id):
    query = account_model.select().where(account_model.c.customer_id == id)
    row = await database.fetch_one(query)
    if row is None:
        return None
    return Account(
        id=row.id,
        balance=row.balance,
        created_at=row.created_at,
        status=row.status,
        customer_id=row.customer_id
    )
    
    