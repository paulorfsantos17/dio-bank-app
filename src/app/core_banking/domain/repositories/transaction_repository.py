from abc import ABC, abstractmethod

from src.app.core_banking.domain.entities.customer import Customer
from src.app.core_banking.domain.entities.transaction import Transaction


class TransactionRepository(ABC):
  @abstractmethod
  def save(self, transaction: Transaction) -> None:
    pass

  @abstractmethod
  def find_by_id(self, id: str) -> Transaction | None:
    pass
  
  
  
