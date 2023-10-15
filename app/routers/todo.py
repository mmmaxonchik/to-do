from fastapi import APIRouter, Depends
from sqlmodel import Session

from controllers.todo import TodoController
from models.database import get_session
from schemas.todo import TodoCreate, TodoGet

router = APIRouter()


@router.post(
    path="",
    response_model=TodoGet,
    summary="Create a new todo",
)
def create_todo(todo: TodoCreate, session: Session = Depends(get_session)) -> TodoGet:
    return TodoGet.parse_obj(TodoController(session).create(todo))
