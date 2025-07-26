from abc import ABC, abstractmethod

from src.app.auth.domain.entities.user import User


class UserRepository(ABC):
  @abstractmethod
  def save(self, user: User):
    pass

  @abstractmethod
  def find_by_id(self, id):
    pass
  
  @abstractmethod
  def find_by_cpf(self, cpf):
    pass
