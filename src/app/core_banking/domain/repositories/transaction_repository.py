from abc import ABC, abstractmethod


class TransactionRepository(ABC):
  @abstractmethod
  def save(self, account):
    pass

  @abstractmethod
  def find_by_id(self, id):
    pass
  
