
from src.app.core_banking.application.use_cases.transfer_founds_use_case import (
    TransferFoundsUseCase,
)
from tests.unit.core_banking.repositories.in_memory.account_repository import (
    InMemoryAccountRepository,
)
from tests.unit.core_banking.repositories.in_memory.transaction_repository import (
    InMemoryTransactionRepository,
)


def make_transfer_founds_use_case():
    in_memory_transaction_repository = InMemoryTransactionRepository()
    in_memory_account_repository = InMemoryAccountRepository()

    open_account_use_case = TransferFoundsUseCase(
        transaction_repository=in_memory_transaction_repository,
        account_repository=in_memory_account_repository
    )

    return open_account_use_case, in_memory_transaction_repository, in_memory_account_repository