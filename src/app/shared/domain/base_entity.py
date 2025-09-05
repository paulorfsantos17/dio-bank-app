from datetime import datetime, timezone

from src.app.shared.domain.objects_values.unique_entity_id import UniqueEntityId


class BaseEntity:
    def __init__(self, id: UniqueEntityId = None, created_at: datetime = None):
        self.id = id or UniqueEntityId()
        self.created_at = created_at or datetime.now(timezone.utc)
        
    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, created_at={self.created_at})"
    
    @property
    def created_at(self):
        return self._created_at
    
    @property
    def id(self) -> UniqueEntityId:
        return self._id
    
    @id.setter
    def id(self, id: UniqueEntityId):
        self._id = id
        
    @created_at.setter
    def created_at(self, created_at: datetime):
        self._created_at = created_at