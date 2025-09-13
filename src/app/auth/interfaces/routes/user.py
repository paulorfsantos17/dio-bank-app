from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.app.auth.application.use_cases.authenticate_user_use_case import (
    AuthenticateUserUseCase,
)
from src.app.auth.application.use_cases.register_user_use_case import (
    RegisterUserUseCase,
)
from src.app.auth.interfaces.controllers.authenticate_controller import (
    AuthenticateUserController,
)
from src.app.auth.interfaces.controllers.register_user_controller import (
    RegisterUserController,
)
from src.app.auth.interfaces.factories.make_authenticate_user_use_case import (
    get_authenticate_user_use_case,
)
from src.app.auth.interfaces.factories.make_register_user_usecase import (
    get_register_user_usecase,
)
from src.app.auth.interfaces.schemas.autheticate_schema import AuthenticateSchema
from src.app.auth.interfaces.schemas.register_user_schema import RegisterUserSchema

routes = APIRouter()

@routes.post("/register", status_code=HTTPStatus.CREATED)
async def register_user(user: RegisterUserSchema, use_case: RegisterUserUseCase = Depends(get_register_user_usecase)):
    register_user_controller = RegisterUserController(use_case)
    return await register_user_controller.execute(user=user)

@routes.post("/auth", status_code=HTTPStatus.OK)
async def register_user(authenticate_user: AuthenticateSchema, use_case: AuthenticateUserUseCase = Depends(get_authenticate_user_use_case)):
    authenticate_user_controller = AuthenticateUserController(use_case)
    return await authenticate_user_controller.execute(authenticate_user=authenticate_user)