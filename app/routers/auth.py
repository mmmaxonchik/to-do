from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from controllers.auth import AuthController
from models.database import get_session
from schemas.auth import Token
from schemas.user import UserGet, UserCreate

router = APIRouter()


@router.post(
    path="/signup",
    response_model=UserGet,
    summary="Signup a new user",
    responses={
        200: {
            "description": "User with this email already exists",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "User with this email already exists"
                    }
                }
            }
        }
    }
)
def register(
        user: UserCreate,
        session: Session = Depends(get_session)
) -> UserGet:
    user = AuthController(session).register(user)
    if user is None:
        raise HTTPException(status_code=200, detail="User with this email already exists")
    return UserGet.parse_obj(user)


@router.post(
    path="/token",
    response_model=Token,
    status_code=200,
    summary="Get access token",
    responses={
        401: {
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Incorrect email or password"
                    }
                }
            }
        }
        
    }
)
def get_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: Session = Depends(get_session)
) -> Token:
    user = AuthController(session).authenticate_user(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return Token(
        access_token=AuthController.create_access_token(
            data={"sub": user.email}
        ),
        token_type="bearer"
    )
