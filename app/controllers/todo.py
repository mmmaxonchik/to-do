from sqlmodel import Session

from models.todo import TodoModel
from schemas.todo import TodoCreate, TodoInDB


class TodoController:
    def __init__(self, session: Session):
        self.session = session
    
    def create(self, todo: TodoCreate) -> TodoInDB:
        session = self.session
        todo_db = TodoModel(**todo.dict())
        session.add(todo_db)
        session.commit()
        session.refresh(todo_db)
        return TodoInDB.from_orm(todo_db)
