from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str = Field(
        title="Token hash",
        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    )
    token_type: str = Field(
        title="Token type",
        example="bearer"
    )
