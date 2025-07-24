from dataclasses import dataclass


@dataclass(frozen=True)
class GetAccountBalanceOutputDTO:
  balance: float
  account_id: str