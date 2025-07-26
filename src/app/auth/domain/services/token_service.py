from abc import ABC, abstractmethod


class TokenService(ABC):
  
  @abstractmethod
  def generate_token(self, user_id: str) -> str:
    pass
  
  @abstractmethod
  def decode_token(self, token: str) -> str:
    pass