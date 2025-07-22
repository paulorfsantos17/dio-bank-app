from datetime import datetime

from app.core_banking.domain.value_objects.money import Money
from src.app.core_banking.domain.value_objects.cpf import CPF
from src.app.shared.domain.base_entity import BaseEntity
from src.app.shared.domain.objects_values.unique_entity_id import UniqueEntityId


class Customer(BaseEntity):
    def __init__(
        self,
        customer_id: UniqueEntityId,
        balance: Money,
        status: bool,
        id: UniqueEntityId = None,
        created_at: datetime = None
    ):
        super().__init__(id=id, created_at=created_at)
        self._customer_id = customer_id
        self._balance = balance
        self._status = status
        
    @property
    def customer_id(self) -> UniqueEntityId:
        return self._customer_id
      
    @property
    def balance(self) -> Money:
        return self._balance
      
    @property
    def status(self) -> bool:
        return self._status
      
    def deposit(self, amount: Money):
        self._balance += amount
    def withdraw(self, amount: Money):
        if amount.amount > self._balance.amount:
            raise ValueError("Insufficient funds")
        self._balance -= amount