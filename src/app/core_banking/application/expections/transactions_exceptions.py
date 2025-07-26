from src.app.core_banking.application.expections.core_banking_error import (
    CoreBankingError,
)


class TransactionError(CoreBankingError):
    """Base para exceções relacionadas a conta."""
    pass

class InsufficientFoundsError(TransactionError):
    def __init__(self, account_id: str):
        super().__init__(f"Insufficient founds in account with ID '{account_id}'")
