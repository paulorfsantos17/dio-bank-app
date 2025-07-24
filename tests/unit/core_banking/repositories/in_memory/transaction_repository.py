from src.app.core_banking.domain.repositories.transaction_repository import (
    TransactionRepository,
)


class InMemoryTransactionRepository(TransactionRepository):
  def __init__(self):
    self.transactions = []

  def save(self, transaction):
    self.transactions.append(transaction)


  def find_by_id(self, id):
    return next(filter(lambda acc: acc.id == id, self.transactions), None)
  

