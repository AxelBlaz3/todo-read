from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends
from functools import lru_cache
from .config.settings import Settings

# Getter for Settings instance.
def get_settings():
    return Settings()


# Getter for mongodb client.
async def get_mongo_client(settings: Settings = Depends(get_settings)):
    return AsyncIOMotorClient(settings.mongodb_url)
