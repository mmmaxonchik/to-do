from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship


class UserModel(SQLModel, table=True):
    # User model in table
    __tablename__ = "user"
    user_id: Optional[int] = Field(primary_key=True, default=None)
    email: str = Field(nullable=False, unique=True)
    name: str = Field(nullable=False)
    hashed_password: str = Field(nullable=False)
    
    todos: List["TodoModel"] = Relationship(back_populates="user")
