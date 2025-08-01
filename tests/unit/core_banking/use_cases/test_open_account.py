import pytest

from src.app.core_banking.application.dto.open_account_input_dto import (
    OpenAccountInputDTO,
)
from src.app.core_banking.application.expections.customer_exceptions import (
    CustomerAlreadyHasAccountError,
    CustomerNotFoundError,
)
from tests.factories.use_cases.open_account_use_case_factory import (
    make_open_account_use_case,
)
from tests.unit.core_banking.repositories.in_memory.account_repository import (
    InMemoryAccountRepository,
)
from tests.unit.core_banking.repositories.in_memory.customer_repository import (
    InMemoryCustomerRepository,
)


def test_open_account_success():
  open_account_use_case, in_memory_customer_repository, in_memory_account_repository = make_open_account_use_case()
  
  in_memory_customer_repository.save(
    InMemoryCustomerRepository.create_customer_with_id("1")
  )
  
  
  data_new_account: OpenAccountInputDTO = OpenAccountInputDTO(
    customer_id="1",
    initial_balance=100.0
  )
  
  result = open_account_use_case.execute(data_new_account)
  
  in_memory_database_account = in_memory_account_repository.find_by_id(result.id)
  
  assert in_memory_database_account is not None
  assert result is not None
  assert result.id is not None
  assert result.id == in_memory_database_account.id
  assert result.customer_id  ==  "1"
  assert result.balance == 100
  
def test_open_account_fail_when_customer_does_not_exist():
  open_account_use_case, in_memory_customer_repository, in_memory_account_repository = make_open_account_use_case()
  
  data_new_account: OpenAccountInputDTO = OpenAccountInputDTO(
    customer_id="not-exist",
    initial_balance=100.0
  )
  
  
  with pytest.raises(CustomerNotFoundError) as exc_info:
        open_account_use_case.execute(data_new_account)

  assert str(exc_info.value) == f"Customer with ID '{data_new_account.customer_id}' not found."
  
  

def test_open_account_fail_when_customer_already_has_an_account():
  open_account_use_case, in_memory_customer_repository, in_memory_account_repository = make_open_account_use_case()
  
  in_memory_customer_repository.save(
    InMemoryCustomerRepository.create_customer_with_id("1")
  )
  
  in_memory_account_repository.save(
    InMemoryAccountRepository.create_account(id="1", customer_id="1", balance=100.0, status=True))
  
  data_new_account: OpenAccountInputDTO = OpenAccountInputDTO(
    customer_id="1",
    initial_balance=100.0
  )
  
  
  with pytest.raises(CustomerAlreadyHasAccountError) as exc_info:
        open_account_use_case.execute(data_new_account)

  assert str(exc_info.value) == f"Customer with ID '{data_new_account.customer_id}' already has an account."
  

