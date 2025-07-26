from dataclasses import dataclass
from datetime import datetime

from src.app.shared.domain.base_entity import BaseEntity
from src.app.shared.domain.objects_values.cpf import CPF
from src.app.shared.domain.objects_values.unique_entity_id import UniqueEntityId


@dataclass
class Customer(BaseEntity):
    def __init__(
        self,
        name: str,
        cpf: CPF,
        id: UniqueEntityId = None,
        created_at: datetime = None
    ):
        super().__init__(id=id, created_at=created_at)
        self._name = name
        self._cpf = cpf

    @property
    def name(self) -> str:
        return self._name

    @property
    def cpf(self) -> CPF:
        return self._cpf


    @name.setter# Exemplo de método que poderia conter alguma regra de negócio
    def name(self, new_name: str):
        if not new_name:
            raise ValueError("Name cannot be empty.")
        self._name = new_name
