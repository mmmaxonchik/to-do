import os
from datetime import timedelta, datetime
from hashlib import sha256
from typing import Union, Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import EmailStr
from sqlmodel import Session

from schemas.user import UserGet, UserCreate, UserInDB
from .user import UserController


class JWTSettings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


class AuthController:
    OAuth2Scheme = OAuth2PasswordBearer(
        tokenUrl="auth/token"
    )
    
    def __init__(self, session: Session):
        self.session = session
    
    @staticmethod
    def get_password_hash(password: str) -> str:
        return sha256(password.encode("utf-8")).hexdigest()
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        plain_password = sha256(plain_password.encode("utf-8")).hexdigest()
        return plain_password == hashed_password
    
    @staticmethod
    def create_access_token(data: dict) -> str:
        expires_delta = timedelta(JWTSettings.ACCESS_TOKEN_EXPIRE_MINUTES)
        data["exp"] = datetime.utcnow() + expires_delta
        return jwt.encode(data, JWTSettings.SECRET_KEY, JWTSettings.ALGORITHM)
    
    @staticmethod
    def is_authorize(token: Annotated[str, Depends(OAuth2Scheme)]) -> None:
        credentials_exception = HTTPException(
            detail="Could not validate credentials",
            status_code=401,
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            token = jwt.decode(
                token,
                JWTSettings.SECRET_KEY,
                algorithms=[JWTSettings.ALGORITHM],
            )
            
            email, exp = token.get("sub"), token.get("exp")
            if datetime.utcnow() > datetime.fromtimestamp(exp):
                raise HTTPException(
                    status_code=401,
                    detail="Token expired",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        
        except (JWTError, ValueError):
            raise credentials_exception
    
    def authenticate_user(self, email: str, password: str) -> Union[UserInDB, None]:
        user = UserController(self.session).get_by_email(EmailStr(email))
        if not user:
            return None
        if self.get_password_hash(password) != user.hashed_password:
            return None
        return user
    
    def register(self, user: UserCreate) -> UserGet | None:
        return UserController(self.session).create(user, self.get_password_hash(user.password))
