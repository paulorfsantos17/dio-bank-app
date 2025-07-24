from src.app.core_banking.application.use_cases.open_account_use_case import (
    OpenAccountUseCase,
)
from tests.unit.core_banking.repositories.in_memory.account_repository import (
    InMemoryAccountRepository,
)
from tests.unit.core_banking.repositories.in_memory.customer_repository import (
    InMemoryCustomerRepository,
)


def make_open_account_use_case():
    in_memory_customer_repository = InMemoryCustomerRepository()
    in_memory_account_repository = InMemoryAccountRepository()

    open_account_use_case = OpenAccountUseCase(
        customer_repository=in_memory_customer_repository,
        account_repository=in_memory_account_repository
    )

    return open_account_use_case, in_memory_customer_repository, in_memory_account_repository