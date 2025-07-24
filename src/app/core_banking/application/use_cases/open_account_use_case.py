from src.app.core_banking.application.dto.open_account_input_dto import (
    OpenAccountInputDTO,
)
from src.app.core_banking.application.expections.customer_exceptions import (
    CustomerAlreadyHasAccountError,
    CustomerNotFoundError,
)
from src.app.core_banking.domain.entities.account import Account
from src.app.core_banking.domain.repositories.account_repository import (
    AccountRepository,
)
from src.app.core_banking.domain.repositories.customer_repository import (
    CustomerRepository,
)


class OpenAccountUseCase:
  def __init__(self, account_repository: AccountRepository, customer_repository: CustomerRepository):
    self.account_repository = account_repository
    self.customer_repository = customer_repository
    
  def execute(self, new_data_account: OpenAccountInputDTO):
    customer = self.customer_repository.find_by_id(new_data_account.customer_id)
    if customer is None:
      raise CustomerNotFoundError(customer_id=new_data_account.customer_id)
    
    has_account = self.account_repository.find_by_customer_id(customer.id)
    
    
    if has_account is not None:
      raise CustomerAlreadyHasAccountError(customer_id=new_data_account.customer_id)
    
    account = Account.create_account(
      id=None,
      customer_id=customer.id,
      balance=new_data_account.initial_balance,
      status=True
    )
    self.account_repository.save(account)
    return account