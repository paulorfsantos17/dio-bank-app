import uuid

from pydantic import BaseModel, Field, field_validator


class GetAccountBalanceSchema(BaseModel):
    account_id : str

    @field_validator("account_id")
    def validate_uuid(cls, v):
        try:
            uuid.UUID(v)
        except ValueError:
            raise ValueError("customer_id precisa ser um UUID válido")
        return v  # retorna como string mesmo