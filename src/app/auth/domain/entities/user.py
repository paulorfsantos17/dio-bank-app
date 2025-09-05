from src.app.auth.domain.value_objects.email import Email
from src.app.shared.domain.base_entity import BaseEntity
from src.app.shared.domain.objects_values.cpf import CPF


class User(BaseEntity):
  def __init__(self, id = None, created_at = None, name: str = None, email: Email = None, password_hash: str = None, cpf: CPF = None):
    super().__init__(id, created_at)
    self._name = name
    self._email = email
    self._password_hash = password_hash
    self._cpf = cpf
    
  
  def __repr__(self):
    return (
        f"User(id={self.id}, "
        f"name='{self._name}', "
        f"email='{self._email}', "
        f"cpf='{self._cpf}')"
    )

  @property
  def name(self):
    return self._name

  @property
  def email(self):
    return self._email
  
  @property
  def cpf(self):
    return self._cpf
  
  @property
  def password_hash(self):
    return self._password_hash
  @email.setter
  def email(self, email: Email):
    self._email = email

  @password_hash.setter
  def password_hash(self, password_hash: str):
    self._password_hash = password_hash
    
  
    
    