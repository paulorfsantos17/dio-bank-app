

from src.app.auth.application.dtos.authenticate_user_input_dto import (
    AuthenticateUserInputDTO,
)
from src.app.auth.application.dtos.authenticate_user_output_dto import (
    AuthenticateUserOutputDTO,
)
from src.app.auth.application.expections.password_exceptions import InvalidPasswordError
from src.app.auth.application.expections.user_exceptions import UserNotFoundError
from src.app.auth.domain.repositories.user_repository import UserRepository
from src.app.auth.domain.services.hash_password_service import HashPasswordService
from src.app.auth.domain.services.token_service import TokenService


class AuthenticateUserUseCase:
  def __init__(self, user_repository: UserRepository, token_service: TokenService, hash_password_service: HashPasswordService):
    self.user_repository = user_repository
    self.token_service = token_service
    self.hash_password_service = hash_password_service
    
  def execute(self,user_authenticate: AuthenticateUserInputDTO) -> AuthenticateUserOutputDTO:
    user = self.user_repository.find_by_cpf(user_authenticate.cpf)
    
    if not user:
      raise UserNotFoundError(user_authenticate.cpf)
    
    if not self.hash_password_service.verify_password(user_authenticate.password, user.password_hash):
      raise InvalidPasswordError()
        
    token = self.token_service.generate_token(str(user.id.value))
    
    return AuthenticateUserOutputDTO(token=token)
  