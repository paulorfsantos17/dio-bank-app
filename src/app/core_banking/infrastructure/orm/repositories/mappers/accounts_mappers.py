import datetime

from app.core_banking.domain.value_objects.money import Money
from app.shared.domain.objects_values.unique_entity_id import UniqueEntityId
from src.app.core_banking.domain.entities.account import Account


class AccountMapper:
    @staticmethod
    def to_record(account: Account) -> dict:
        return {
            "id": str(account.id.value),
            "customer_id": str(account.customer_id.value),
            "balance": account.balance.value(),
            "status": account.status,
            "created_at": account.created_at or datetime.utcnow()
        }

    @staticmethod
    def from_record(row: dict) -> Account:
        return Account(
            id=UniqueEntityId(str(row["id"])),
            customer_id=UniqueEntityId(str(row["customer_id"])),
            balance=Money(row["balance"]),
            status=row["status"],
            created_at=row["created_at"]
        )