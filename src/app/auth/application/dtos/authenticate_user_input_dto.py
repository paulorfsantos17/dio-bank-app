
from dataclasses import dataclass


@dataclass(frozen=True)
class AuthenticateUserInputDTO:
  cpf: str
  password: str