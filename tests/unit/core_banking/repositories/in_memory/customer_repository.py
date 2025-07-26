from src.app.core_banking.domain.entities.customer import Customer
from src.app.core_banking.domain.repositories.customer_repository import (
    CustomerRepository,
)
from src.app.shared.domain.objects_values.cpf import CPF


class InMemoryCustomerRepository(CustomerRepository):
  customers: list[Customer]
  def __init__(self):
    self.customers = []

  def save(self, customer):
    self.customers.append(customer)

  def find_by_id(self, id):
    return next(filter(lambda acc: acc.id == id, self.customers), None)
  
  def find_by_cpf(self, cpf):
    return next(filter(lambda acc: acc.cpf == cpf, self.customers), None)
  

  @staticmethod
  def create_customer_with_id(customer_id: str = "1") -> Customer:
      return Customer(
        id=customer_id,
        name="John Doe",
        cpf=CPF("123.456.789-00"),
  )
