from fastapi import HTTPException, status

from src.app.auth.interfaces.schemas.register_user_schema import RegisterUserSchema
from src.app.core_banking.application.dto.transfer_funds_input_dto import (
    TransferFundsInputDTO,
)
from src.app.core_banking.application.expections.account_exceptions import (
    AccountNotFoundError,
)
from src.app.core_banking.application.expections.transactions_exceptions import (
    InsufficientFoundsError,
)
from src.app.core_banking.application.use_cases.transfer_founds_use_case import (
    TransferFoundsUseCase,
)
from src.app.core_banking.interfaces.schemas.transfer_founds_schema import (
    TransferFoundsSchema,
)


class TransferAccountsFundsController:
    def __init__(self, make_transfer_founds_use_case: TransferFoundsUseCase):
        self.make_transfer_founds_use_case = make_transfer_founds_use_case  
    
    async def execute(self, transfer_data: TransferFoundsSchema):
        try:
            transfer_founds_input_DTO   =  TransferFundsInputDTO(
                **transfer_data.model_dump()
            )
            await self.make_transfer_founds_use_case.execute(data_transfer_founds=transfer_founds_input_DTO)
            return {"message": "Transferencia realizada com sucesso"}
        
        except AccountNotFoundError as ae:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(ae)
            )
        except InsufficientFoundsError as ae:
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
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Erro interno do servidor"
            )
