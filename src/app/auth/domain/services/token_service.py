from abc import ABC, abstractmethod


class TokenService(ABC):
  
  @abstractmethod
  def generate_token(self, user_id: str) -> str:
    pass
  
