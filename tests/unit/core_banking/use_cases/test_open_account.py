import pytest

from src.app.core_banking.application.dto.open_account_input_dto import (
    OpenAccountInputDTO,
)
from src.app.core_banking.application.expections.customer_exceptions import (
    CustomerAlreadyHasAccountError,
    CustomerNotFoundError,
)
from src.app.core_banking.domain.entities.account import Account
from tests.factories.use_cases.open_account_use_case_factory import (
    make_open_account_use_case,
)
from tests.unit.core_banking.repositories.in_memory.account_repository import (
    InMemoryAccountRepository,
)
from tests.unit.core_banking.repositories.in_memory.customer_repository import (
    InMemoryCustomerRepository,
)


async def test_open_account_success():
  open_account_use_case, in_memory_customer_repository, in_memory_account_repository = make_open_account_use_case()
  
  await in_memory_customer_repository.save(
    InMemoryCustomerRepository.create_customer_with_id("1")
  )
  
  
  data_new_account: OpenAccountInputDTO = OpenAccountInputDTO(
    customer_id="1",
    initial_balance=100.0
  )
  
  result =  await  open_account_use_case.execute(data_new_account)
  
  in_memory_database_account = await in_memory_account_repository.find_by_id(result.id)
  
  assert in_memory_database_account is not None
  assert result is not None
  assert result.id is not None
  assert result.id == in_memory_database_account.id
  assert result.customer_id.value  ==  "1"
  assert result.balance.value() == 100
  
async def test_open_account_fail_when_customer_does_not_exist():
  open_account_use_case, _, _ = make_open_account_use_case()
  
  data_new_account: OpenAccountInputDTO = OpenAccountInputDTO(
    customer_id="not-exist",
    initial_balance=100.0
  )
  
  
  with pytest.raises(CustomerNotFoundError) as exc_info:
        await open_account_use_case.execute(data_new_account)

  assert str(exc_info.value) == f"Customer with ID '{data_new_account.customer_id}' not found."
  
  

async def test_open_account_fail_when_customer_already_has_an_account():
  open_account_use_case, in_memory_customer_repository, in_memory_account_repository = make_open_account_use_case()
  
  await in_memory_customer_repository.save(
    InMemoryCustomerRepository.create_customer_with_id("1")
  )
  
  await in_memory_account_repository.save(
    Account.create_account(id="1", customer_id="1", balance=100.0, status=True))
  
  data_new_account: OpenAccountInputDTO = OpenAccountInputDTO(
    customer_id="1",
    initial_balance=100.0
  )
  
  
  with pytest.raises(CustomerAlreadyHasAccountError) as exc_info:
        await open_account_use_case.execute(data_new_account)

  assert str(exc_info.value) == f"Customer with ID '{data_new_account.customer_id}' already has an account."
  

