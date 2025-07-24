from src.app.core_banking.application.use_cases.get_account_balance_use_case import (
    GetAccountBalanceUseCase,
)
from tests.unit.core_banking.repositories.in_memory.account_repository import (
    InMemoryAccountRepository,
)


def make_get_account_balance_use_case():
  in_memory_account_repository = InMemoryAccountRepository()

  get_account_balance_use_case = GetAccountBalanceUseCase(
    account_repository=in_memory_account_repository,
  )

  return get_account_balance_use_case, in_memory_account_repository