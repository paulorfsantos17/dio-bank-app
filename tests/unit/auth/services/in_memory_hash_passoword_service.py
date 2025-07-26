from src.app.auth.domain.services.hash_password_service import HashPasswordService


class InMemoryHashPasswordService(HashPasswordService):
  
  def hash_password(self, plain_password: str) -> str:
    return plain_password + "-hashed"
  
  def verify_password(self, plain_password: str, hashed_password: str) -> bool:
    return plain_password + "-hashed" == hashed_password