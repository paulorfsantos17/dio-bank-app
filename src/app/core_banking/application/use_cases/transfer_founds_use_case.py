from datetime import datetime

from src.app.core_banking.application.dto.transfer_funds_input_dto import (
    TransferFundsInputDTO,
)
from src.app.core_banking.application.expections.account_exceptions import (
    AccountNotFoundError,
)
from src.app.core_banking.application.expections.transactions_exceptions import (
    InsufficientFoundsError,
)
from src.app.core_banking.domain.entities.transaction import Transaction
from src.app.core_banking.domain.repositories.account_repository import (
    AccountRepository,
)
from src.app.core_banking.domain.repositories.transaction_repository import (
    TransactionRepository,
)
from src.app.core_banking.domain.value_objects.money import Money


class TransferFoundsUseCase:
  def __init__(self, account_repository: AccountRepository, transaction_repository: TransactionRepository):
    self.account_repository = account_repository
    self.transaction_repository = transaction_repository
    
  def execute(self, data_transfer_founds: TransferFundsInputDTO):
    account_from = self.account_repository.find_by_id(data_transfer_founds.account_from)
    if account_from is None:
      raise AccountNotFoundError(account_id=data_transfer_founds.account_from)
    
    account_to = self.account_repository.find_by_id(data_transfer_founds.account_to)
    
    if  account_to is None:
      raise AccountNotFoundError(account_id=data_transfer_founds.account_to)
    
    if(account_from.balance.value() < data_transfer_founds.amount):
      raise InsufficientFoundsError(account_id=data_transfer_founds.account_from)
    
    
    account_from.withdraw(Money(data_transfer_founds.amount)) 
    account_to.deposit(Money(data_transfer_founds.amount)) 
    
    transaction = Transaction(
      account_from=account_from.id,
      account_to=account_to.id,
      amount=data_transfer_founds.amount,
      timestamp=  datetime.now().timestamp()
    )
    
    self.transaction_repository.save(
      transaction
    )
    
    return transaction