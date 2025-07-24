from src.app.core_banking.application.expections.core_banking_error import (
    CoreBankingError,
)


class AccountError(CoreBankingError):
    """Base para exceções relacionadas a conta."""
    pass

class AccountNotFoundError(AccountError):
    def __init__(self, account_id: str):
        super().__init__(f"Account with ID '{account_id}' not found.")
