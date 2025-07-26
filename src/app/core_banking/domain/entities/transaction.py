from datetime import datetime

from src.app.core_banking.domain.value_objects.money import Money
from src.app.shared.domain.base_entity import BaseEntity
from src.app.shared.domain.objects_values.unique_entity_id import UniqueEntityId


class Transaction(BaseEntity):
    def __init__(
        self,
        account_from: UniqueEntityId,
        account_to: UniqueEntityId,
        amount: Money,
        timestamp: datetime,
        id: UniqueEntityId = None,
        created_at: datetime = None,
    ):
        super().__init__(id=id, created_at=created_at)
        self.account_from = account_from
        self.account_to = account_to
        self.amount = amount
        self.timestamp = timestamp 