from typing import Union

from pydantic import EmailStr
from sqlmodel import Session

from models.user import UserModel
from schemas.user import UserGet, UserInDB


class UserController:
    def __init__(self, session: Session):
        self.session = session
    
    def get_by_id(self, user_id: int) -> UserGet | None:
        return self.session.query(UserModel).filter(UserModel.user_id == user_id).first()
    
    def get_all(self):
        return self.session.query(UserModel).all()
    
    def get_by_email(self, email: EmailStr) -> Union[UserInDB, None]:
        orm_user = self.session.query(UserModel).filter(UserModel.email == email).first()
        if orm_user is None:
            return None
        return UserInDB.from_orm(orm_user)
    
    def create(self, user: UserInDB) -> UserGet | None:
        session = self.session
        if self.get_by_email(user.email):
            return None
        user_db = UserModel(name=user.name, email=user.email, hashed_password=user.hashed_password)
        session.add(user_db)
        session.commit()
        session.refresh(user_db)
        return self.get_by_email(user.email)
