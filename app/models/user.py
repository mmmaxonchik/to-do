from sqlmodel import Field, SQLModel
from typing import Optional


class UserModel(SQLModel, table=True):
    # User models in table
    __tablename__ = "user"
    user_id: Optional[int] = Field(primary_key=True, default=None)
    email: str = Field(nullable=False, unique=True)
    name: str = Field(nullable=False)
    hashed_password: str = Field(nullable=False)
