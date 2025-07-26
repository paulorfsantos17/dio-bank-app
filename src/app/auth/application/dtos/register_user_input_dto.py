
from dataclasses import dataclass


@dataclass(frozen=True)
class RegisterUserInputDTO:
  name: str
  email: str
  password: str
  cpf: str