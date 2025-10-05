import uuid

from pydantic import BaseModel, Field, field_validator

from src.app.shared.validators.uuid_validator import ensure_uuid


class GetAccountBalanceSchema(BaseModel):
    account_id : str

    @field_validator("account_id")
    def validate_uuid_account_id(cls, v):
        return ensure_uuid(v)