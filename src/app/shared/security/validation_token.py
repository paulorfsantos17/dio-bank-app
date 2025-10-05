import ast

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.app.shared.config.settings import settings

security = HTTPBearer()

SECRET_KEY = settings.jwt_token

def validate_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = ast.literal_eval(credentials.credentials)
    try:
        payload = jwt.decode(token['token'], SECRET_KEY, algorithms=["HS256"])
        return payload  # retorna dados do usuário
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )