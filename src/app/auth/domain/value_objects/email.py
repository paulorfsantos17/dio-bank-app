import re


class InvalidEmailError(ValueError):
    pass

class Email:
    def __init__(self, value: str):
        if not self._is_valid(value):
            raise InvalidEmailError(f"E-mail inválido: {value}")
        self._value = value.lower()

    @staticmethod
    def _is_valid(email: str) -> bool:
        # Regex simples para validação de e-mail
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other) -> bool:
        if not isinstance(other, Email):
            return False
        return self._value == other._value

    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return f"Email('{self._value}')"