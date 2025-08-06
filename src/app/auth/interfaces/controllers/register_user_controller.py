from fastapi import HTTPException, status

from src.app.auth.application.dtos.register_user_input_dto import RegisterUserInputDTO
from src.app.auth.application.use_cases.register_user_use_case import (
    RegisterUserUseCase,
)
from src.app.auth.interfaces.schemas.register_user_schema import RegisterUserSchema


class RegisterUserController:
    def __init__(self, register_user_use_case: RegisterUserUseCase):
        self.register_user_use_case = register_user_use_case  
    
    def execute(self, user: RegisterUserSchema):
        try:
            dto = RegisterUserInputDTO(**user.model_dump())
            result = self.register_user_use_case.execute(dto)
            return {"message": "User registered successfully", "user_id": result.id}
        
        except ValueError as ve:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))
        
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
