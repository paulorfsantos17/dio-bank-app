# core_banking/domain/value_objects/cpf.py
import re


class CPF:
    def __init__(self, cpf: str):
        if not self._is_valid(cpf):
            raise ValueError(f"CPF inválido: {cpf}")
        self._value = cpf

    @property
    def value(self) -> str:
        return self._value

    def _is_valid(self, cpf: str) -> bool:
        # Aqui um exemplo simples só para ilustrar (validação real é mais complexa)
        pattern = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
        return re.match(pattern, cpf) is not None

    def __eq__(self, other):
        if not isinstance(other, CPF):
            return False
        return self._value == other._value

    def __str__(self):
        return self._value
