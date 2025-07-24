from dataclasses import dataclass


@dataclass(frozen=True)
class OpenAccountInputDTO:
  customer_id: str
  initial_balance: float | None