
from dataclasses import dataclass


@dataclass(frozen=True)
class AuthenticateUserOutputDTO:
  token: str