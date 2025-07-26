

from src.app.auth.application.dtos.register_user_input_dto import RegisterUserInputDTO
from src.app.auth.application.expections.user_exceptions import AlreadyExistsUserError
from src.app.auth.domain.entities.user import User
from src.app.auth.domain.repositories.user_repository import UserRepository
from src.app.auth.domain.services.hash_password_service import HashPasswordService


class RegisterUserUseCase:
  def __init__(self, user_repository: UserRepository, hash_password_service: HashPasswordService):
    self.user_repository = user_repository
    self.hash_password_service = hash_password_service

  
  def execute(self, user: RegisterUserInputDTO):
    user_exists = self.user_repository.find_by_cpf(user.cpf)
    
    if(user_exists):
      raise AlreadyExistsUserError(str(user_exists.id.value))
    
    password_hash = self.hash_password_service.hash_password(user.password)
    
    new_user = User(
      name = user.name,
      email = user.email,
      password_hash= password_hash,
      cpf = user.cpf
    )
    
    
    self.user_repository.save(new_user)
    
    
    return None