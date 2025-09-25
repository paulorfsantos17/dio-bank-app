
from httpx import AsyncClient

from src.app.auth.domain.entities.user import User
from src.app.auth.infrastructure.orm.repositories.user_repository_sql_alchemy import (
    UserRepositorySqlAlchemy,
)
from src.app.auth.infrastructure.services.hash_password_bcrypt_service import (
    HashPasswordBCryptdService,
)
from src.app.core_banking.infrastructure.orm.repositories.account_repository_sqlalchemy import (
    AccountRepositorySQLAlchemy,
)


async def test_open_account_e2e_success(client: AsyncClient):
    hash_password_service = HashPasswordBCryptdService()
    user_in_db= User(
        name="Jose Doe",
        email="jose.doe@test.com",
        password_hash=hash_password_service.hash_password("Teste@123"),
        cpf="955.476.220-87"
    )
    
    repo_user = UserRepositorySqlAlchemy()
    await repo_user.save(user_in_db)


    
    payload = {
        "customer_id": user_in_db.id.value,
        "initial_balance": 100,
    }
    
    response = await client.post("/accounts", json=payload)
    assert response.status_code == 201

    repo_account = AccountRepositorySQLAlchemy()
    account_in_db = await repo_account.find_by_customer_id(payload["customer_id"])
    assert account_in_db is not None
    assert account_in_db.customer_id.value == user_in_db.id.value
    assert account_in_db.balance.value() == payload["initial_balance"]
