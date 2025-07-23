from src.app.core_banking.domain.repositories.account_repository import (
    AccountRepository,
)


class InMemoryAccountRepository(AccountRepository):
  def __init__(self):
    self.accounts = []

  def save(self, account):
    self.accounts.append(account)

  def find_by_id(self, id):
    return next(filter(lambda acc: acc.id == id, self.accounts), None)
  

