from src.app.auth.application.expections.auth_exceptions import AuthBaseException


class InvalidPasswordError(AuthBaseException):
  def __init__(self):
    super().__init__("Invalid password.")
