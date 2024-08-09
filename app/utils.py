# app/utils.py
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "6df6e58ffaf7b238d6d54684a14f12c7480015d4d8467dcd784c2b7f143924b0"
ALGORITHM = "HS256"
EXPIRE_TIME = 20


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(EXPIRE_TIME)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="util_functions"
)
