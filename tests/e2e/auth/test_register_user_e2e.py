
from httpx import AsyncClient

from src.app.auth.infrastructure.orm.repositories.user_repository_sql_alchemy import (
    UserRepositorySqlAlchemy,
)


async def test_register_user_e2e_success(client: AsyncClient):
    payload = {
        "name": "Ana Clara Souza",
        "email": "ana.clara.souza@test.com",
        "password": "Teste1234",
        "cpf": "168.995.350-09"
    }

    response = await client.post("/register", json=payload)
    assert response.status_code == 201

    repo_user = UserRepositorySqlAlchemy()
    user_in_db = await repo_user.find_by_cpf(payload["cpf"])

    assert user_in_db is not None
    assert user_in_db.email == payload["email"]
