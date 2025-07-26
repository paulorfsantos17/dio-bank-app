from abc import ABC, abstractmethod

from src.app.core_banking.domain.entities.account import Account


class AccountRepository(ABC):
  @abstractmethod
  def save(self, account) -> None:
    pass

  @abstractmethod
  def find_by_id(self, id) -> Account | None:
    pass
  
  @abstractmethod
  def find_by_customer_id(self, id) -> Account | None:
    pass
  

