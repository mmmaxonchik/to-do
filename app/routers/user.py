from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from controllers.auth import AuthController
from controllers.user import UserController
from models.database import get_session
from schemas.user import UserGet

# Create router for user
router = APIRouter()


# Get all users
@router.get(
    path="",
    response_model=List[UserGet],
    summary="Get all users",
)
def get_all(
        session: Session = Depends(get_session),
        is_auth: bool = Depends(AuthController.is_authorize)
) -> List[UserGet]:
    return [UserGet.parse_obj(user) for user in UserController(session).get_all()]


# Get user by user_id
@router.get(
    path="/{user_id}",
    response_model=UserGet,
    summary="Get one user by user_id",
    responses={
        404: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "User not found"
                    }
                }
            }
        }
        
    }
)
def get_by_id(
        user_id: int,
        session: Session = Depends(get_session),
        is_auth: bool = Depends(AuthController.is_authorize)
) -> UserGet:
    user = UserController(session).get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserGet.parse_obj(user)
