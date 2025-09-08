from src.app.auth.domain.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
  def __init__(self):
    self.users = []

  async def save(self, user):
    self.users.append(user)

  async def find_by_id(self, id):
    return next(filter(lambda acc: acc.id == id, self.users), None)
  
  async def find_by_cpf(self, cpf):
    return next(filter(lambda acc: acc.cpf == cpf, self.users), None) 
  

