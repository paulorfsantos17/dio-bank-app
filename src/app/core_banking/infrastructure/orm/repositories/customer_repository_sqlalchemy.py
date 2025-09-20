
from src.app.core_banking.domain.entities.customer import Customer
from src.app.core_banking.domain.repositories.customer_repository import (
    CustomerRepository,
)
from src.app.shared.database.database_config import database
from src.app.shared.database.models.user import user as user_model
from src.app.shared.domain.objects_values.unique_entity_id import UniqueEntityId


class CustomerRepositorySQLAlchemy(CustomerRepository):

    async def find_by_id(self, id):
        query = user_model.select().where(user_model.c.id == id)
        row = await database.fetch_one(query)
        if row is None:
            return None
        return Customer(
            id=UniqueEntityId(str(row.id)) if row.id else None,
            name=row.name,
            cpf=row.cpf,
            created_at=row.created_at,
        )
        
    async def find_by_cpf(self, cpf):
        query = user_model.select().where(user_model.c.cpf == cpf)
        row = await database.fetch_one(query)
        if row is None:
            return None
        return Customer(
            id=row.id,
            name=row.name,
            cpf=row.cpf,
            created_at=row.created_at,
        )
    
    async def save(self, customer: Customer):
        query = user_model.insert().values(
            id=customer.id.value,
            name=customer.name,
            cpf=customer.cpf,
            created_at=customer.created_at
        )
        await database.execute(query)
    