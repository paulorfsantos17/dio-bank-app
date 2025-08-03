from jwt import decode, encode

from src.app.auth.domain.services.token_service import TokenService
from src.app.shared.config.settings import config


class TokenJWTService(TokenService):
  def generate_token(self, user_id: str):
    token = encode({"user_id": user_id}, config.jwt_token, algorithm="HS256")
    return token
  
  def decode_token(self, token):
    data = decode(token, config.jwt_token, algorithms=["HS256"])
    
    return data