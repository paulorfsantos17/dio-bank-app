import uuid

from pydantic import BaseModel, field_validator

from src.app.shared.validators.uuid_validator import ensure_uuid


class TransferFoundsSchema(BaseModel):
    account_from : str
    account_to : str
    amount : float

    @field_validator("account_from")
    def validate_uuid_account_from(cls, v):
        return ensure_uuid(v)
    @field_validator("account_to")
    def validate_uuid_account_to(cls, v):
        return ensure_uuid(v)