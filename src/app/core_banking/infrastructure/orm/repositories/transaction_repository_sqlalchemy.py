
from src.app.core_banking.domain.entities.transaction import Transaction
from src.app.core_banking.domain.repositories.transaction_repository import (
    TransactionRepository,
)
from src.app.core_banking.infrastructure.orm.models.transaction import transaction_model
from src.app.core_banking.infrastructure.orm.repositories.mappers.transaction_mappers import (
    TransactionMapper,
)
from src.app.shared.database.database_config import database


class TransactionRepositorySQLAlchemy(TransactionRepository):
  async def save(self, transaction):
    transaction_row = TransactionMapper.to_record(transaction)
    
    
    query = transaction_model.insert().values(
        id=transaction_row['id'],
        amount=transaction_row['amount'],
        account_from=transaction_row['account_from'],
        account_to=transaction_row['account_to'],
        created_at=transaction_row['created_at'],
        timestamp=transaction_row['timestamp'],
    )
    
    await database.execute(query)
    
    

    
  async def find_by_id(self, id):
    query = transaction_model.select().where(transaction_model.c.id == id)  
    row = await database.fetch_one(query)
    if row is None:
        return None
    return TransactionMapper.from_record(row)