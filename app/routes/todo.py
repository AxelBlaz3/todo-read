from fastapi.routing import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.results import InsertOneResult
from fastapi import Depends
from fastapi.exceptions import HTTPException
from ..dependencies import get_mongo_client

from ..models.todo import Todo


router = APIRouter()

@router.get("/todos")
async def get_all_todos(client: AsyncIOMotorClient = Depends(get_mongo_client)):
    return await client.tododb.todos.find().to_list(20)


@router.get("/todo/{id}")
async def  get_todo(id: str, client: AsyncIOMotorClient = Depends(get_mongo_client)):
    todo = await client.tododb.todos.find_one({'_id': id})
    
    if todo:
        return todo
    
    raise HTTPException(status_code=404, detail=f'Todo {id} not found.')
