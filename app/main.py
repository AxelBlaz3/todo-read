from fastapi import FastAPI
from .routes import todo

# Create a FastAPI app.
app = FastAPI()

# Include todo router.
app.include_router(todo.router)