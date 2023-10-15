from fastapi import FastAPI
from routers import users, auth
from models.database import create_all_tables

# Create tables
create_all_tables()

# Create exemplar of app
app = FastAPI()

# Bind routers to app
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
