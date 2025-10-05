from uuid import uuid4

from src.app.core_banking.domain.entities.account import Account
from src.app.core_banking.domain.value_objects.money import Money


class InMemoryAccountRepository:
    def __init__(self):
        # simula uma tabela: {id: Account}
        self._storage: dict[str, Account] = {}

    async def save(self, account: Account) -> Account:
        # garante que balance é Money
        balance_vo = account.balance if isinstance(account.balance, Money) else Money(account.balance)

        new_account = Account(
            id=account.id or str(uuid4()),
            customer_id=account.customer_id,
            balance=balance_vo,
            status=account.status,
        )
        self._storage[new_account.id.value] = new_account
        return new_account

    async def find_by_id(self, account_id: str) -> Account | None:
        return self._storage.get(str(account_id))

    async def find_by_customer_id(self, customer_id: str) -> Account | None:
        # retorna a primeira conta que encontrar para o customer_id
        for account in self._storage.values():
            if str(account.customer_id) == str(customer_id):
                return account
        return None
    
    async def update(self, account_id: str, **kwargs) -> Account | None:
        stored_account = self._storage.get(str(account_id))
        if stored_account:
            for key, value in kwargs.items():
                if hasattr(stored_account, key):
                    setattr(stored_account, key, value)
            return stored_account
        return None
    async def all(self) -> list[Account]:
        return list(self._storage.values())