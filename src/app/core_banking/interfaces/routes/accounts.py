from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.app.core_banking.application.use_cases.get_account_balance_use_case import (
    GetAccountBalanceUseCase,
)
from src.app.core_banking.application.use_cases.open_account_use_case import (
    OpenAccountUseCase,
)
from src.app.core_banking.application.use_cases.transfer_founds_use_case import (
    TransferFoundsUseCase,
)
from src.app.core_banking.interfaces.controllers.get_account_balance_controller import (
    GetAccountBalanceController,
)
from src.app.core_banking.interfaces.controllers.open_account_controller import (
    OpenAccountController,
)
from src.app.core_banking.interfaces.controllers.transfer_accounts_funds_controller import (
    TransferAccountsFundsController,
)
from src.app.core_banking.interfaces.factories.make_get_account_balance_use_case import (
    make_get_account_balance_use_case,
)
from src.app.core_banking.interfaces.factories.make_open_accont_use_case import (
    get_open_account_use_case,
)
from src.app.core_banking.interfaces.factories.make_transfer_founds_use_case import (
    make_transfer_funds_use_case,
)
from src.app.core_banking.interfaces.schemas.open_account_schema import (
    OpenAccountSchema,
)
from src.app.core_banking.interfaces.schemas.transfer_founds_schema import (
    TransferFoundsSchema,
)
from src.app.shared.security.validation_token import validate_token

routes_accounts = APIRouter(prefix="/accounts")

@routes_accounts.post("", status_code=HTTPStatus.CREATED)
async def open_account(open_account: OpenAccountSchema, use_case: OpenAccountUseCase = Depends(get_open_account_use_case)):
    open_account_controller= OpenAccountController(use_case)
    return await open_account_controller.execute(account=open_account)

@routes_accounts.get("/{account_id}/balance", status_code=HTTPStatus.OK, dependencies=[Depends(validate_token)] )
async def open_account(account_id: str, use_case: GetAccountBalanceUseCase = Depends(make_get_account_balance_use_case)):
    get_account_balance_controller= GetAccountBalanceController(use_case)
    return await get_account_balance_controller.execute(account_id=account_id)
    reponse = await client.post("/accounts/transactions", json=payload)
@routes_accounts.post("/transactions", status_code=HTTPStatus.OK, dependencies=[Depends(validate_token)])
async def open_account(transfer_data: TransferFoundsSchema, use_case: TransferFoundsUseCase = Depends(make_transfer_funds_use_case)):
    transfer_accounts_funds_controller= TransferAccountsFundsController(use_case)
    return await transfer_accounts_funds_controller.execute(transfer_data=transfer_data)


