from fastapi import APIRouter

from app.auth.interfaces.schemas.register_user_schema import RegisterUserSchema
from src.app.auth.interfaces.controllers.register_user_controller import (
    RegisterUserController,
)
from src.app.auth.interfaces.factories.make_register_user_usecase import (
    get_register_user_usecase,
)

routes = APIRouter()

@routes.post("/register")
async def register_user(user: RegisterUserSchema):
  register_user_controller = RegisterUserController(get_register_user_usecase)
  return register_user_controller.execute(user=user)