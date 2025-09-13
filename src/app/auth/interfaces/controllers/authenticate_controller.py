from fastapi import HTTPException, status

from src.app.auth.application.dtos.authenticate_user_input_dto import (
    AuthenticateUserInputDTO,
)
from src.app.auth.application.expections.password_exceptions import InvalidPasswordError
from src.app.auth.application.expections.user_exceptions import UserNotFoundByCpfError
from src.app.auth.application.use_cases.authenticate_user_use_case import (
    AuthenticateUserUseCase,
)
from src.app.auth.interfaces.schemas.autheticate_schema import AuthenticateSchema


class AuthenticateUserController:
    def __init__(self, authenticate_user_use_case: AuthenticateUserUseCase):
        self.authenticate_user_use_case = authenticate_user_use_case  
    
    async def execute(self, authenticate_user: AuthenticateSchema):
        
        try:
            dto = AuthenticateUserInputDTO(**authenticate_user.model_dump())
            access_token = await self.authenticate_user_use_case.execute(dto)
            return {"access_token": access_token}
        
        except UserNotFoundByCpfError as ae:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str("Usuario ou senha incorretos.")
            )
        except InvalidPasswordError as ae:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str("Usuario ou senha incorretos.")
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
