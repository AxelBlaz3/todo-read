from fastapi.routing import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.results import InsertOneResult
from fastapi import Depends
from fastapi.exceptions import HTTPException
from ..dependencies import get_mongo_client

from ..models.todo import Todo


router = APIRouter()

# Endpoint for getting all todos.
@router.get("/todos")
async def get_all_todos(client: AsyncIOMotorClient = Depends(get_mongo_client)):
    return await client.tododb.todos.find().to_list(20)

# Endpoint for getting a specific todo based on id.
@router.get("/todo/{id}")
async def  get_todo(id: str, client: AsyncIOMotorClient = Depends(get_mongo_client)):
    # Make a query in the DB with given id.
    todo = await client.tododb.todos.find_one({'_id': id})
    
    # Check if todo exists.
    if todo:
        return todo
    
    # If not, raise an exception with 404.
    raise HTTPException(status_code=404, detail=f'Todo {id} not found.')
