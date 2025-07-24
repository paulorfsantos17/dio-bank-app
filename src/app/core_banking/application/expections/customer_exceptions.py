from src.app.core_banking.application.expections.core_banking_error import (
    CoreBankingError,
)


class CustomerError(CoreBankingError):
    """Base para exceções relacionadas ao cliente."""
    pass

class CustomerNotFoundError(CustomerError):
    def __init__(self, customer_id: str):
        super().__init__(f"Customer with ID '{customer_id}' not found.")

class CustomerAlreadyHasAccountError(CustomerError):
    def __init__(self, customer_id: str):
        super().__init__(f"Customer with ID '{customer_id}' already has an account.")