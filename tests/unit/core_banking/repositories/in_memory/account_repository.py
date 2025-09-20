from src.app.core_banking.domain.entities.account import Account
from src.app.core_banking.domain.repositories.account_repository import (
    AccountRepository,
)


class InMemoryAccountRepository(AccountRepository):
  accounts: list[Account]
  def __init__(self):
    self.accounts = []

  async def save(self, account):
    self.accounts.append(account)

  async def find_by_id(self, id):
    return next(filter(lambda acc: acc.id == id, self.accounts), None)
  
  async def find_by_customer_id(self, id):
    return next(filter(lambda acc: acc.customer_id == id, self.accounts), None)
  
  async def update(self, account):
    for index, acc in enumerate(self.accounts):
      if acc.id == account.id:
        self.accounts[index] = account
  
  @staticmethod
  def create_account(id: str, customer_id: str, balance: float, status: bool):
    return Account(
      id=id or "1",
      customer_id=customer_id or "1",
      balance=balance or 100.0,
      status=status or True
  )

