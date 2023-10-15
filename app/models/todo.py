from typing import Optional

from sqlmodel import Field, SQLModel, Relationship

from models.user import UserModel


class TodoModel(SQLModel, table=True):
    # TodoModel in table
    __tablename__ = "todo"
    todo_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False, index=True)
    description: Optional[str] = Field(default=None)
    is_done: bool = Field(default=False)
    
    user_id: Optional[int] = Field(default=None, foreign_key="user.user_id")
    user: Optional[UserModel] = Relationship(back_populates="todos")
