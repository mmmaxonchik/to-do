from pydantic import BaseModel
from fastapi.responses import JSONResponse


class Message(BaseModel):
    message: str
    
    
def create_message(status_code: int, message: str) -> JSONResponse:
    return JSONResponse(status_code=status_code, content={
        "message": message
    })

