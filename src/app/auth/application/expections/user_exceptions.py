from src.app.auth.application.expections.auth_exceptions import AuthBaseException


class AlreadyExistsUserByCpfError(AuthBaseException):
  def __init__(self, cpf: str):
    super().__init__(f"User with cpf '{cpf}' already exists.")

class UserNotFoundByIdError(AuthBaseException):
  def __init__(self, id: str):
    super().__init__(f"User with id '{id}' not found.")
class UserNotFoundByCpfError(AuthBaseException):
  def __init__(self, cpf: str):
    super().__init__(f"User with cpf '{cpf}' not found.")