from src.app.core_banking.domain.entities.transaction import Transaction
from src.app.core_banking.domain.value_objects.money import Money
from src.app.core_banking.infrastructure.orm.models.transaction import transaction_model
from src.app.shared.domain.objects_values.unique_entity_id import UniqueEntityId


class TransactionMapper:
    @staticmethod
    def to_record(transaction: Transaction) -> dict:
        return {
            "id": transaction.id.value,
            "amount": transaction.amount.value(),
            "account_from": transaction.account_from.value,
            "account_to": transaction.account_to.value,
            "created_at": transaction.created_at,
            "timestamp": transaction.timestamp,
        }

    @staticmethod
    def from_record(row) -> Transaction:
        return Transaction(
            id=UniqueEntityId(str(row.id)),
            amount=Money(row.amount),
            account_from=UniqueEntityId(str(row.account_from)),
            account_to=UniqueEntityId(str(row.account_to)),
            created_at=row.created_at,
            timestamp=row.timestamp,
        )
