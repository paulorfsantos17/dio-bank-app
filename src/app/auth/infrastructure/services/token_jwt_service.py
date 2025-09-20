from jwt import encode

from src.app.auth.domain.services.token_service import TokenService
from src.app.shared.config.settings import settings


class TokenJWTService(TokenService):
  def generate_token(self, user_id: str):
    token = encode({"user_id": user_id}, settings.jwt_token, algorithm="HS256")
    return token
  
