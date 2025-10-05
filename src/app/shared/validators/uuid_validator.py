import uuid


def ensure_uuid(v):
  try:
      uuid.UUID(v)
  except ValueError:
      raise ValueError("customer_id precisa ser um UUID válido")
  return v  # retorna como string mesmo