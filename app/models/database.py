from os import getenv

from sqlmodel import create_engine, Session

# Get ENV - FASTAPI_DB_URL from virtual env
DATABASE_URL = getenv('FASTAPI_DB_URL')

# Create engine for db connection
engine = create_engine(
    DATABASE_URL,
)


def create_all_tables():
    from models.todo import TodoModel
    from models.todo import UserModel
    TodoModel.metadata.create_all(bind=engine)
    UserModel.metadata.create_all(bind=engine)


# Function for create sessions
def get_session():
    with Session(engine) as session:
        yield session
