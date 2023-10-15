from typing import Union, List

from pydantic import EmailStr
from sqlmodel import Session

from models.user import UserModel
from schemas.user import UserInDB, UserCreate


class UserController:
    def __init__(self, session: Session):
        self.session = session
    
    def get_by_id(self, user_id: int) -> Union[UserInDB, None]:
        orm_user = self.session.query(UserModel).filter(UserModel.user_id == user_id).first()
        if orm_user is None:
            return None
        return UserInDB.from_orm(orm_user)
    
    def get_all(self) -> List[UserInDB]:
        return [UserInDB.from_orm(orm_user) for orm_user in self.session.query(UserModel).all()]
    
    def get_by_email(self, email: EmailStr) -> Union[UserInDB, None]:
        orm_user = self.session.query(UserModel).filter(UserModel.email == email).first()
        if orm_user is None:
            return None
        return UserInDB.from_orm(orm_user)
    
    def create(self, user: UserCreate, hashed_password: str) -> UserInDB | None:
        session = self.session
        if self.get_by_email(user.email):
            return None
        user_db = UserModel(name=user.name, email=user.email, hashed_password=hashed_password)
        session.add(user_db)
        session.commit()
        session.refresh(user_db)
        return self.get_by_email(user.email)
