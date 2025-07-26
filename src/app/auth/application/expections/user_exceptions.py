from src.app.auth.application.expections.auth_exceptions import AuthBaseException


class AlreadyExistsUserError(AuthBaseException):
  def __init__(self, id: str):
    super().__init__(f"User with id '{id}' already exists.")

class UserNotFoundError(AuthBaseException):
  def __init__(self, cpf: str):
    super().__init__(f"User with cpf '{cpf}' not found.")