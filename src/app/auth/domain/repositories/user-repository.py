from abc import ABC, abstractmethod


class UserRepository(ABC):
  @abstractmethod
  def save(self, account):
    pass

  @abstractmethod
  def find_by_id(self, id):
    pass
  
  @abstractmethod
  def find_by_cpf(self, cpf):
    pass
