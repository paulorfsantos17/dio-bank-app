import pytest

from src.app.auth.application.dtos.register_user_input_dto import RegisterUserInputDTO
from src.app.auth.application.expections.user_exceptions import AlreadyExistsUserError
from src.app.auth.domain.entities.user import User
from tests.factories.use_cases.register_use_case_factory import (
    make_register_user_use_case,
)


def test_register_user_success():
  register_user_use_case, in_memory_user_repository,in_memory_hash_password_service  = make_register_user_use_case()
  
  raw_password = "123456"
  data_register_user: RegisterUserInputDTO = RegisterUserInputDTO(
    name="John Doe",
    email="test@example.com",
    password=raw_password,
    cpf="123.456.789-00"
  )
  
  register_user_use_case.execute(data_register_user)
  
  assert len(in_memory_user_repository.users) == 1
  assert in_memory_user_repository.users[0].name == data_register_user.name
  assert in_memory_user_repository.users[0].email == data_register_user.email
  assert in_memory_user_repository.users[0].cpf == data_register_user.cpf
  assert in_memory_user_repository.users[0].password_hash is not None
  assert in_memory_user_repository.users[0].created_at is not None
  assert in_memory_user_repository.users[0].password_hash == in_memory_hash_password_service.hash_password(raw_password)

def test_register_user_fail_user_already_exists():
  register_user_use_case, in_memory_user_repository, _ = make_register_user_use_case()
  
  in_memory_user_repository.save(
    User(
      name="John Doe",
      email="test@example.com",
      password_hash="123456-hashed",
      cpf="123.456.789-00"
    )
  )
  
  raw_password = "123456"
  data_register_user: RegisterUserInputDTO = RegisterUserInputDTO(
    name="John Doe",
    email="test@example.com",
    password=raw_password,
    cpf="123.456.789-00"
  )
  
  
  with pytest.raises(AlreadyExistsUserError) as exc_info:
    register_user_use_case.execute(data_register_user)
    
  user = in_memory_user_repository.find_by_cpf(data_register_user.cpf) 
  
  assert str(exc_info.value) == f"User with id '{str(user.id.value)}' already exists."
  

  
  
  