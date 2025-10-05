from src.app.core_banking.domain.entities.transaction import Transaction
from src.app.core_banking.domain.repositories.transaction_repository import (
    TransactionRepository,
)


class InMemoryTransactionRepository(TransactionRepository):
  transactions : list[Transaction]
  def __init__(self):
    self.transactions = []

  async def save(self, transaction):
    self.transactions.append(transaction)
    
  
  
  async def find_by_id(self, id):
    return next(filter(lambda acc: acc.id == id, self.transactions), None)
  
  
  
  

  @staticmethod
  def create_transaction(account_from: str, account_to: str, amount: float, timestamp: str):
    return Transaction(account_from=account_from, account_to=account_to, amount=amount, timestamp=timestamp)
