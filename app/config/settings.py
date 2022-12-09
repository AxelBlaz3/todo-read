from pydantic import BaseSettings

class Settings(BaseSettings):
    """Class for storing environment variables."""
    mongodb_url: str = "mongodb://localhost:27017"

    class Config:
        env_file = '.env'
