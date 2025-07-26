
from src.app.core_banking.domain.entities.transaction import Transaction
from src.app.core_banking.domain.repositories.transaction_repository import (
    TransactionRepository,
)
from src.app.core_banking.infrastructure.orm.models.transaction import transaction_model
from src.app.shared.database.database_config import database


class TransactionRepositorySQLAlchemy(TransactionRepository):
  async def save(self, transaction):
    query = transaction_model.insert().values(
        amount=transaction.amount,
        account_from=transaction.account_from,
        account_to=transaction.account_to,
        created_at=transaction.created_at,
        timestamp=transaction.timestamp
    )
    
    await database.execute(query)
    
  async def find_by_id(self, id):
    query = transaction_model.select().where(transaction_model.c.id == id)  
    row = await database.fetch_one(query)
    if row is None:
        return None
    return Transaction(
        id=row.id,
        amount=row.amount,
        account_from=row.account_from,
        account_to=row.account_to,
        created_at=row.created_at,
        timestamp=row.timestamp
    )