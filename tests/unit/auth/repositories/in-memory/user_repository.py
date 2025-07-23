from app.auth.domain.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
  def __init__(self):
    self.users = []

  def save(self, user):
    self.users.append(user)

  def find_by_id(self, id):
    return next(filter(lambda acc: acc.id == id, self.users), None)
  

