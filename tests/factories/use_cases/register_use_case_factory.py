
from src.app.auth.application.use_cases.register_user_use_case import (
    RegisterUserUseCase,
)
from tests.unit.auth.repositories.in_memory.user_repository import (
    InMemoryUserRepository,
)
from tests.unit.auth.services.in_memory_hash_passoword_service import (
    InMemoryHashPasswordService,
)


def make_register_user_use_case():
    in_memory_user_repository = InMemoryUserRepository()
    in_memory_hash_password_service = InMemoryHashPasswordService()
    
    register_user_use_case = RegisterUserUseCase(
        user_repository=in_memory_user_repository,
        hash_password_service=in_memory_hash_password_service
    )

    return register_user_use_case, in_memory_user_repository, in_memory_hash_password_service