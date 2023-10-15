from fastapi import FastAPI

from routers import user, auth, todo

# Create exemplar of app
app = FastAPI()


# Create tables
@app.on_event("startup")
def create_db():
    from models.database import create_all_tables
    create_all_tables()


# Bind routers to app
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(todo.router, prefix="/todos", tags=["Todo"])
