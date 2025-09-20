from fastapi import HTTPException, status

from src.app.auth.application.dtos.register_user_input_dto import RegisterUserInputDTO
from src.app.auth.application.expections.user_exceptions import (
    AlreadyExistsUserByCpfError,
)
from src.app.auth.interfaces.schemas.register_user_schema import RegisterUserSchema
from src.app.core_banking.application.dto.open_account_input_dto import (
    OpenAccountInputDTO,
)
from src.app.core_banking.application.expections.customer_exceptions import (
    CustomerAlreadyHasAccountError,
    CustomerNotFoundError,
)
from src.app.core_banking.application.use_cases.open_account_use_case import (
    OpenAccountUseCase,
)
from src.app.core_banking.interfaces.schemas.open_account_schema import (
    OpenAccountSchema,
)


class OpenAccountController:
    def __init__(self, open_account_use_case: OpenAccountUseCase):
        self.open_account_use_case = open_account_use_case  
    
    async def execute(self, account: OpenAccountSchema):
        try:
            dto = OpenAccountInputDTO(**account.model_dump())
            new_account = await self.open_account_use_case.execute(dto)
            return {"message": "User registered successfully", "account_id": new_account.id.value}
        
        except CustomerNotFoundError as ae:
            # Erro de negócio -> retorna 400
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(ae)
            )
        except CustomerAlreadyHasAccountError as ae:
            # Erro de negócio -> retorna 400
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
