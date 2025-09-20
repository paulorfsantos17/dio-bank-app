from src.app.core_banking.application.use_cases.open_account_use_case import (
    OpenAccountUseCase,
)
from src.app.core_banking.infrastructure.orm.repositories.account_repository_sqlalchemy import (
    AccountRepositorySQLAlchemy,
)
from src.app.core_banking.infrastructure.orm.repositories.customer_repository_sqlalchemy import (
    CustomerRepositorySQLAlchemy,
)


def get_open_account_use_case():
    account_repository = AccountRepositorySQLAlchemy()
    customer_repository = CustomerRepositorySQLAlchemy()
    return OpenAccountUseCase(account_repository=account_repository, customer_repository=customer_repository)