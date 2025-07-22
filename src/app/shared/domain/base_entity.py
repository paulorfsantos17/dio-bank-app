from datetime import datetime, UTC
from src.app.shared.domain.objects_values.unique_entity_id import UniqueEntityId

class BaseEntity:
    def __init__(self, id: UniqueEntityId = None, created_at: datetime = None):
        self.id = id or UniqueEntityId()
        self.created_at = created_at or datetime.now(UTC)