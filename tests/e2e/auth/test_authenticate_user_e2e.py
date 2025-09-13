
from httpx import AsyncClient

from src.app.auth.domain.entities.user import User
from src.app.auth.infrastructure.orm.repositories.user_repository_sql_alchemy import (
    UserRepositorySqlAlchemy,
)
from src.app.auth.infrastructure.services.hash_password_bcrypt_service import (
    HashPasswordBCryptdService,
)


async def test_authenticate_user_e2e_success(client: AsyncClient):
    hash_password_service = HashPasswordBCryptdService()
    user_in_db= User(
        name="Jose Doe",
        email="jose.doe@test.com",
        password_hash=hash_password_service.hash_password("Teste@123"),
        cpf="899.850.130-93"
    )
    
    payload = {
        "cpf": "899.850.130-93",
        "password": "Teste@123"
    }
    
    repo_user = UserRepositorySqlAlchemy()
    await repo_user.save(user_in_db)

    response = await client.post("/auth", json=payload)
    
    assert response.status_code == 200
    assert response.json()["access_token"]
