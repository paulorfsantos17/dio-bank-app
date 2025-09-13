from src.app.auth.application.use_cases.authenticate_user_use_case import (
    AuthenticateUserUseCase,
)
from src.app.auth.infrastructure.orm.repositories.user_repository_sql_alchemy import (
    UserRepositorySqlAlchemy,
)
from src.app.auth.infrastructure.services.hash_password_bcrypt_service import (
    HashPasswordBCryptdService,
)
from src.app.auth.infrastructure.services.token_jwt_service import TokenJWTService


def get_authenticate_user_use_case():
    user_repository = UserRepositorySqlAlchemy()
    hash_password_service = HashPasswordBCryptdService()
    token_service = TokenJWTService()
    return AuthenticateUserUseCase(user_repository,token_service,hash_password_service)