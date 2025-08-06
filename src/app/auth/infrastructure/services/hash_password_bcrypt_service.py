import bcrypt

from src.app.auth.domain.services.hash_password_service import HashPasswordService


class HashPasswordBCryptdService(HashPasswordService):
  def hash_password(self, plain_password: str) -> str:
    password_hash = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
    return password_hash
  
  def verify_password(self, plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
  