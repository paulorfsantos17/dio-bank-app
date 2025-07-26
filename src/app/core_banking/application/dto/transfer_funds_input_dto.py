from dataclasses import dataclass


@dataclass(frozen=True)
class TransferFundsInputDTO:
  account_from: str
  account_to: str
  amount: float