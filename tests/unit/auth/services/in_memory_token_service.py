from src.app.auth.domain.services.hash_password_service import HashPasswordService
from src.app.auth.domain.services.token_service import TokenService


class InMemoryTokenService(TokenService):
  
  def generate_token(self, user_id: str) -> str:
    return user_id + "-token"
  
  def decode_token(self, token: str) -> str:
    return token.split("-")[0]