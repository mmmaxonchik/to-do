from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(
        title="User name",
        description="Name of the user",
        example="Name"
    )
    email: EmailStr = Field(
        title="User email",
        description="Email of the user",
        example="usermail@edu.hse.ru",
    )


class UserCreate(UserBase):
    password: str = Field(
        title="User password",
        description="Password of the user",
        example="HelloWorld2023!"
    )


class UserInDB(UserBase):
    user_id: Optional[int] = None
    hashed_password: str = Field(
        title="User hashed_password",
        description="Hash from password of the user"
    )
    
    class Config:
        orm_mode = True


class UserGet(UserBase):
    user_id: int = Field(
        title="User id",
        description="Id of the current user",
        example=1
    )
    
    class Config:
        from_attributes = True
