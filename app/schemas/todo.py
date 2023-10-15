from typing import Optional

from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    title: str = Field(
        title="Todo title",
        description="Title of the todo",
        example="Learn Math"
    )
    user_id: Optional[int] = Field(
        title="Todo owner id",
        description="Id of the todo owner",
        example=1
    )


class TodoCreate(TodoBase):
    description: Optional[str] = Field(
        title="Todo description",
        description="Some description for todo",
        example="Todo something"
    )


class TodoGet(TodoBase):
    todo_id: Optional[int] = Field(
        title="Todo id",
        description="Id of the todo",
        example=1
    )
    description: Optional[str] = Field(
        title="Todo description",
        description="Some description for todo",
        example="Todo something"
    )
    is_done: bool = Field(
        title="Todo is done?",
        description="True or False",
        example=True
    )


class TodoInDB(TodoGet):
    class Config:
        orm_mode = True
