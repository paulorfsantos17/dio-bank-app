from dataclasses import dataclass


@dataclass(frozen=True)
class GetAccountBalanceInputDTO:
  id: str