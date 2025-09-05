

from src.app.auth.application.dtos.register_user_input_dto import RegisterUserInputDTO
from src.app.auth.application.expections.user_exceptions import (
    AlreadyExistsUserByCpfError,
)
from src.app.auth.domain.entities.user import User
from src.app.auth.domain.repositories.user_repository import UserRepository
from src.app.auth.domain.services.hash_password_service import HashPasswordService


class RegisterUserUseCase:
  def __init__(self, user_repository: UserRepository, hash_password_service: HashPasswordService):
    self.user_repository = user_repository
    self.hash_password_service = hash_password_service

  
  async def execute(self, user: RegisterUserInputDTO):
    user_exists = await self.user_repository.find_by_cpf(user.cpf)
    if(user_exists is  not None):
      raise AlreadyExistsUserByCpfError(str(user_exists.cpf))
    
    
    
    password_hash = self.hash_password_service.hash_password(user.password)
    
    new_user = User(
      name = user.name,
      email = user.email,
      password_hash= password_hash,
      cpf = user.cpf
    )
    
    
    
    await self.user_repository.save(new_user)

    id = new_user.id.value
    return id