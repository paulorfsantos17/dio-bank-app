import uuid

from pydantic import BaseModel, Field, field_validator


class OpenAccountSchema(BaseModel):
    customer_id : str
    initial_balance : float = Field(..., ge=0, description="O valor inicial deve se maior que zero.")

    @field_validator("customer_id")
    def validate_uuid(cls, v):
        try:
            uuid.UUID(v)
        except ValueError:
            raise ValueError("customer_id precisa ser um UUID válido")
        return v  # retorna como string mesmo