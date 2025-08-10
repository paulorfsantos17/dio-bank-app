from fastapi import APIRouter, Depends

from src.app.auth.application.use_cases.register_user_use_case import (
    RegisterUserUseCase,
)
from src.app.auth.interfaces.controllers.register_user_controller import (
    RegisterUserController,
)
from src.app.auth.interfaces.factories.make_register_user_usecase import (
    get_register_user_usecase,
)
from src.app.auth.interfaces.schemas.register_user_schema import RegisterUserSchema

routes = APIRouter()

@routes.post("/register")
async def register_user(user: RegisterUserSchema, use_case: RegisterUserUseCase = Depends(get_register_user_usecase)):
    register_user_controller = RegisterUserController(use_case)
    return await register_user_controller.execute(user=user)