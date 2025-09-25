from httpx import AsyncClient

from src.app.auth.domain.entities.user import User
from src.app.auth.infrastructure.orm.repositories.user_repository_sql_alchemy import (
    UserRepositorySqlAlchemy,
)
from src.app.core_banking.domain.entities.account import Account
from src.app.core_banking.infrastructure.orm.repositories.account_repository_sqlalchemy import (
    AccountRepositorySQLAlchemy,
)


async def test_get_balance_account_e2e_success(client: AsyncClient):
  user = User(
    name="Jose Doe",
    email="jose.doe@test.com",
    password_hash="Teste@123",
    cpf="955.476.220-87"
  )
  
  
  user_repo =   UserRepositorySqlAlchemy()
  await user_repo.save(user)
  
  account = Account.create_account(id=None, customer_id=user.id, balance=100.0, status=True)
  
  
  account_repo =  AccountRepositorySQLAlchemy()
  await account_repo.save(account)
  
  response = await client.get(f'/accounts/{account.id.value}/balance')
  assert response.status_code == 200
  assert response.json()['balance'] == 100
  assert response.json()['account_id'] == account.id.value