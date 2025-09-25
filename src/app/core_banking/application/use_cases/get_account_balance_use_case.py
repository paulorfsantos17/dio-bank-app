from src.app.core_banking.application.dto.get_account_balance_output_dto import (
    GetAccountBalanceOutputDTO,
)
from src.app.core_banking.application.expections.account_exceptions import (
    AccountNotFoundError,
)
from src.app.core_banking.domain.repositories.account_repository import (
    AccountRepository,
)


class GetAccountBalanceUseCase:
  def __init__(self, account_repository: AccountRepository):
    self.account_repository = account_repository
    
  
  async def execute(self, account_id) -> GetAccountBalanceOutputDTO:
    account = await self.account_repository.find_by_id(account_id)
    if account is None:
      raise AccountNotFoundError(account_id=account_id)
    
    return GetAccountBalanceOutputDTO(
      balance=account.balance.value(),
      account_id=account.id.value
    )