from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends
from functools import lru_cache
from .config.settings import Settings

# @lru_cache()
def get_settings():
    return Settings()


async def get_mongo_client(settings: Settings = Depends(get_settings)):
    return AsyncIOMotorClient(settings.mongodb_url)
