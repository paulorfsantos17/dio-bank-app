from src.app.core_banking.application.use_cases.transfer_founds_use_case import (
    TransferFoundsUseCase,
)
from src.app.core_banking.infrastructure.orm.repositories.account_repository_sqlalchemy import (
    AccountRepositorySQLAlchemy,
)
from src.app.core_banking.infrastructure.orm.repositories.transaction_repository_sqlalchemy import (
    TransactionRepositorySQLAlchemy,
)


def make_transfer_funds_use_case():
    account_repository = AccountRepositorySQLAlchemy()
    transaction_repository = TransactionRepositorySQLAlchemy()
    return TransferFoundsUseCase(account_repository=account_repository, transaction_repository=transaction_repository)