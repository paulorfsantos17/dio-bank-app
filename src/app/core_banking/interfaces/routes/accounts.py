from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.app.auth.interfaces.schemas.autheticate_schema import AuthenticateSchema
from src.app.core_banking.application.use_cases.open_account_use_case import (
    OpenAccountUseCase,
)
from src.app.core_banking.interfaces.controllers.open_account_controller import (
    OpenAccountController,
)
from src.app.core_banking.interfaces.factories.make_open_accont_use_case import (
    get_open_account_use_case,
)
from src.app.core_banking.interfaces.schemas.open_account_schema import (
    OpenAccountSchema,
)

routes_accounts = APIRouter(prefix="/accounts")

@routes_accounts.post("", status_code=HTTPStatus.CREATED)
async def open_account(open_account: OpenAccountSchema, use_case: OpenAccountUseCase = Depends(get_open_account_use_case)):
    open_account_controller = OpenAccountController(use_case)
    return await open_account_controller.execute(account=open_account)
  

