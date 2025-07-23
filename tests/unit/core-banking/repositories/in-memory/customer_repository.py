from src.app.core_banking.domain.repositories.customer_repository import (
    CustomerRepository,
)


class InMemoryCustomerRepository(CustomerRepository):
  def __init__(self):
    self.customers = []

  def save(self, customer):
    self.customers.append(customer)

  def find_by_id(self, id):
    return next(filter(lambda acc: acc.id == id, self.customers), None)
  

