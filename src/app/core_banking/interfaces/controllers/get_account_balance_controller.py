from fastapi import HTTPException, status

from src.app.auth.interfaces.schemas.register_user_schema import RegisterUserSchema
from src.app.core_banking.application.dto.get_account_balance_input_dto import (
    GetAccountBalanceInputDTO,
)
from src.app.core_banking.application.expections.account_exceptions import (
    AccountNotFoundError,
)
from src.app.core_banking.application.use_cases.get_account_balance_use_case import (
    GetAccountBalanceUseCase,
)


class GetAccountBalanceController:
    def __init__(self, get_account_balance_use_case: GetAccountBalanceUseCase):
        self.get_account_balance_use_case = get_account_balance_use_case  
    
    async def execute(self, account_id: str):
        try:
            get_account_balance_input_DTO    = GetAccountBalanceInputDTO(id=account_id)
            get_account_balance_output_DTO = await self.get_account_balance_use_case.execute(account_id=get_account_balance_input_DTO.id)
            return {"balance": get_account_balance_output_DTO.balance, "account_id": get_account_balance_output_DTO.account_id}
        
        except AccountNotFoundError as ae:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(ae)
            )
        

        except ValueError as ve:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(ve)
            )

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Erro interno do servidor"
            )
