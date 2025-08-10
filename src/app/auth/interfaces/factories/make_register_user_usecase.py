from src.app.auth.application.use_cases.register_user_use_case import (
    RegisterUserUseCase,
)
from src.app.auth.infrastructure.orm.repositories.user_repository_sql_alchemy import (
    UserRepositorySqlAlchemy,
)
from src.app.auth.infrastructure.services.hash_password_bcrypt_service import (
    HashPasswordBCryptdService,
)
from src.app.auth.infrastructure.services.token_jwt_service import TokenJWTService


def get_register_user_usecase():
    user_repository = UserRepositorySqlAlchemy()
    hash_password_service = HashPasswordBCryptdService()
    return RegisterUserUseCase(user_repository,hash_password_service)