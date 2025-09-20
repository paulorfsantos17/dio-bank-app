import pytest

from src.app.core_banking.application.dto.get_account_balance_input_dto import (
    GetAccountBalanceInputDTO,
)
from src.app.core_banking.application.expections.account_exceptions import (
    AccountNotFoundError,
)
from tests.factories.use_cases.get_account_balance_use_case_factory import (
    make_get_account_balance_use_case,
)
from tests.unit.core_banking.repositories.in_memory.account_repository import (
    InMemoryAccountRepository,
)


async def test_get_account_balance_use_case_success():
  get_account_balance_use_case, in_memory_account_repository= make_get_account_balance_use_case()
  account = InMemoryAccountRepository.create_account(id="1", customer_id="1", balance=100.0, status=True)
  
  await in_memory_account_repository.save(account)

  

  data_get_account_balance: GetAccountBalanceInputDTO = GetAccountBalanceInputDTO(
    id="1"
  )
  
  
  result  = await  get_account_balance_use_case.execute(account_id=data_get_account_balance.id)
  
  account_from_repo = await in_memory_account_repository.find_by_id(data_get_account_balance.id)
    
  assert account_from_repo.balance == 100
  
  assert  result.balance. == 100


async def test_get_account_balance_use_case_fail_when_account_does_not_exist():
  get_account_balance_use_case, _ = make_get_account_balance_use_case()
  
  data_get_account_balance: GetAccountBalanceInputDTO = GetAccountBalanceInputDTO(
    id="not-exist"
  )
  
  with pytest.raises(AccountNotFoundError) as exc_info:
    await get_account_balance_use_case.execute(account_id=data_get_account_balance.id)
  
  assert str(exc_info.value) == f"Account with ID '{data_get_account_balance.id}' not found."