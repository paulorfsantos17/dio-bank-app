from abc import ABC, abstractmethod

from src.app.core_banking.domain.entities.customer import Customer


class CustomerRepository(ABC):
  @abstractmethod
  def save(self, customer: Customer) -> None:
    pass

  @abstractmethod
  def find_by_id(self, id) -> Customer | None:
    pass
  
  @abstractmethod
  def find_by_cpf(self, cpf) -> Customer | None:
    pass
