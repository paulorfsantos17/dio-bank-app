
from httpx import AsyncClient

from app.core_banking.domain.entities.account import Account
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


async def test_transfer_funds_e2e_success(client: AsyncClient, access_token: str):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    user_one = User(
        name="Jose Doe",
        email="jose.doe@test.com",
        password_hash="Teste@123",
        cpf="955.476.220-87"
    )
    user_two = User(
        name="John Doe 2",
        email="john.doe2@test.com",
        password_hash="Teste@123",
        cpf="123.456.789-00"
    )
    
    
    repo_user = UserRepositorySqlAlchemy()
    await repo_user.save(user_one)
    await repo_user.save(user_two)
    
    account_one = Account.create_account(id=None, customer_id=user_one.id, balance=100.0, status=True)
    account_two = Account.create_account(id=None, customer_id=user_two.id, balance=100.0, status=True)
    
    repo_account = AccountRepositorySQLAlchemy()
    
    await repo_account.save(account_one)
    await repo_account.save(account_two)
    
    payload = {
        "account_from": account_one.id.value,
        "account_to": account_two.id.value,
        "amount": 50.0
        
    }

    reponse = await client.post("/accounts/transactions", json=payload, headers=headers)
    assert reponse.status_code == 200
    data = reponse.json()
    assert data["message"] == "Transferencia realizada com sucesso"
    
    
    updated_account_one = await repo_account.find_by_id(payload["account_from"])
    updated_account_two = await repo_account.find_by_id(payload["account_to"])
    
    assert updated_account_one.balance.value() == 50.0
    assert updated_account_two.balance.value() == 150.0
