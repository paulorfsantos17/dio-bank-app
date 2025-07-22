from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class BaseDTO(BaseModel):
    id: UUID
    created_at: datetime
