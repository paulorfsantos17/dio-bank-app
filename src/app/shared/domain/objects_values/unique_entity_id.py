import uuid

class UniqueEntityId:
    def __init__(self, id: str = None):
        if id is None:
            self._value = str(uuid.uuid4())
        else:
            # aqui você pode adicionar validação para o id recebido (por exemplo, UUID válido)
            self._value = id

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other):
        if not isinstance(other, UniqueEntityId):
            return False
        return self._value == other._value

    def __str__(self):
        return self._value

    def __repr__(self):
        return f"UniqueEntityId({self._value})"
