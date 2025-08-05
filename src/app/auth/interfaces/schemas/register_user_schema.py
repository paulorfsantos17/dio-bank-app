from pydantic import BaseModel


class RegisterUserSchema(BaseModel):
  name: str
  email: str
  password: str
  cpf: str