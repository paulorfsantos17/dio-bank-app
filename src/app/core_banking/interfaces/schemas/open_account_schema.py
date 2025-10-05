from pydantic import BaseModel, Field, field_validator

from src.app.shared.validators.uuid_validator import ensure_uuid


class OpenAccountSchema(BaseModel):
    customer_id : str
    initial_balance : float = Field(..., ge=0, description="O valor inicial deve se maior que zero.")

    @field_validator("customer_id")
    def validate_uuid_customer_id(cls, v):
        return ensure_uuid(v)