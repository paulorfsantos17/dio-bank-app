import pytest

from src.app.auth.application.dtos.authenticate_user_input_dto import (
    AuthenticateUserInputDTO,
)
from src.app.auth.application.expections.password_exceptions import InvalidPasswordError
from src.app.auth.application.expections.user_exceptions import UserNotFoundError
from src.app.auth.domain.entities.user import User
from tests.factories.use_cases.authenticat_user import make_authenticate_user_use_case


def test_authenticate_user_success():
  authenticate_user_use_case, in_memory_user_repository,in_memory_hash_password_service, in_memory_token_service  =make_authenticate_user_use_case()
  user =  User(
      name="John Doe",
      email="test@example.com",
      password_hash=in_memory_hash_password_service.hash_password("123456"),
      cpf="123.456.789-00"
    )
  in_memory_user_repository.save(
    user
  )
  
  data_user_login: AuthenticateUserInputDTO = AuthenticateUserInputDTO(
    cpf="123.456.789-00",
    password="123456"
  )
  
  
  
  result = authenticate_user_use_case.execute(data_user_login)
  
  assert result is not None
  assert result.token is not None
  assert result.token == in_memory_token_service.generate_token(str(user.id.value))
  
def test_authenticate_user_fail_user_not_found():
  authenticate_user_use_case, _, _, _  =make_authenticate_user_use_case()
  
  data_user_login: AuthenticateUserInputDTO = AuthenticateUserInputDTO(
    cpf="123.456.789-00",
    password="12345678"
  )
  
  
  with pytest.raises(UserNotFoundError) as exc_info:
    authenticate_user_use_case.execute(data_user_login)
  
  assert str(exc_info.value) == f"User with cpf '{data_user_login.cpf}' not found."

def test_authenticate_user_fail_invalid_password():
  authenticate_user_use_case, in_memory_user_repository,in_memory_hash_password_service, in_memory_token_service  =make_authenticate_user_use_case()
  user =  User(
      name="John Doe",
      email="test@example.com",
      password_hash=in_memory_hash_password_service.hash_password("123456"),
      cpf="123.456.789-00"
    )
  in_memory_user_repository.save(
    user
  )
  
  data_user_login: AuthenticateUserInputDTO = AuthenticateUserInputDTO(
    cpf="123.456.789-00",
    password="12345678"
  )
  
  
  
  with pytest.raises(InvalidPasswordError) as exc_info:
    authenticate_user_use_case.execute(data_user_login)
  
  assert str(exc_info.value) == "Invalid password."
