from src.app.core_banking.application.use_cases.get_account_balance_use_case import (
    GetAccountBalanceUseCase,
)
from src.app.core_banking.infrastructure.orm.repositories.account_repository_sqlalchemy import (
    AccountRepositorySQLAlchemy,
)


def make_get_account_balance_use_case():
    account_repository = AccountRepositorySQLAlchemy()
    return GetAccountBalanceUseCase(account_repository=account_repository)