from pydantic import BaseSettings

class Settings(BaseSettings):
    mongodb_url: str = "mongodb://mongo:27017"

    class Config:
        env_file = '.env'
