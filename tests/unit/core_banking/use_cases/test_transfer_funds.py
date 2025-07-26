import pytest

from src.app.core_banking.application.dto.transfer_funds_input_dto import (
    TransferFundsInputDTO,
)
from src.app.core_banking.application.expections.account_exceptions import (
    AccountNotFoundError,
)
from src.app.core_banking.application.expections.transactions_exceptions import (
    InsufficientFoundsError,
)
from src.app.core_banking.domain.value_objects.money import Money
from tests.factories.use_cases.transfer_founds_use_case_factory import (
    make_transfer_founds_use_case,
)
from tests.unit.core_banking.repositories.in_memory.account_repository import (
    InMemoryAccountRepository,
)


def test_transfer_founds_use_case_sucess():
  open_account_use_case, in_memory_transaction_repository, in_memory_account_repository = make_transfer_founds_use_case()
  account_from = InMemoryAccountRepository.create_account(id="1", customer_id="1", balance=Money(100.0), status=True)
  account_to = InMemoryAccountRepository.create_account(id="2", customer_id="1", balance=Money(100.0), status=True)
  
  in_memory_account_repository.save(account_from)
  
  in_memory_account_repository.save(account_to)
  
  
  data_transfer_founds: TransferFundsInputDTO = TransferFundsInputDTO(
    account_from="1",
    account_to="2",
    amount=100.0
  )
  
  result = open_account_use_case.execute(data_transfer_founds)
  
  in_memory_database_transaction = in_memory_transaction_repository.find_by_id(result.id)
  
  
  assert in_memory_database_transaction is not None
  assert result is not None
  
  assert result.account_from == "1"
  assert result.account_to == "2"
  assert result.amount == 100
  assert in_memory_account_repository.find_by_id(data_transfer_founds.account_from).balance == Money(0)
  assert in_memory_account_repository.find_by_id(data_transfer_founds.account_to).balance == Money(200)

def test_transfer_founds_use_case_fail_with_insufficient_funds():
  open_account_use_case, _ ,in_memory_account_repository = make_transfer_founds_use_case()
  account_from = InMemoryAccountRepository.create_account(id="1", customer_id="1", balance=Money(50.0), status=True)
  account_to = InMemoryAccountRepository.create_account(id="2", customer_id="1", balance=Money(0), status=True)
  
  in_memory_account_repository.save(account_from)
  
  in_memory_account_repository.save(account_to)
  
  
  data_transfer_founds: TransferFundsInputDTO = TransferFundsInputDTO(
    account_from="1",
    account_to="2",
    amount=100.0
  )
  with pytest.raises(InsufficientFoundsError) as exc_info:
    open_account_use_case.execute(data_transfer_founds)
    
  assert str(exc_info.value) == f"Insufficient founds in account with ID '{data_transfer_founds.account_from}'"
  
  

def test_transfer_founds_use_case_fail_with_account_to_not_found():
  open_account_use_case, _ ,in_memory_account_repository = make_transfer_founds_use_case()
  account_from = InMemoryAccountRepository.create_account(id="1", customer_id="1", balance=Money(100.0), status=True)
  
  in_memory_account_repository.save(account_from)
  
  
  
  data_transfer_founds: TransferFundsInputDTO = TransferFundsInputDTO(
    account_from="1",
    account_to="2",
    amount=100.0
  )
  with pytest.raises(AccountNotFoundError) as exc_info:
    open_account_use_case.execute(data_transfer_founds)
    
  assert str(exc_info.value) == f"Account with ID '{data_transfer_founds.account_to}' not found."
  