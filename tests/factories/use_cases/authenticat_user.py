
from src.app.auth.application.use_cases.authenticate_user_use_case import (
    AuthenticateUserUseCase,
)
from src.app.auth.application.use_cases.register_user_use_case import (
    RegisterUserUseCase,
)
from tests.unit.auth.repositories.in_memory.user_repository import (
    InMemoryUserRepository,
)
from tests.unit.auth.services.in_memory_hash_passoword_service import (
    InMemoryHashPasswordService,
)
from tests.unit.auth.services.in_memory_token_service import InMemoryTokenService


def make_authenticate_user_use_case():
    in_memory_user_repository = InMemoryUserRepository()
    in_memory_hash_password_service = InMemoryHashPasswordService()
    in_memory_token_service = InMemoryTokenService()
    
    
    authenticate_user_use_case = AuthenticateUserUseCase(
        user_repository=in_memory_user_repository,
        hash_password_service=in_memory_hash_password_service,
        token_service=in_memory_token_service
    )

    return authenticate_user_use_case, in_memory_user_repository, in_memory_hash_password_service,in_memory_token_service 