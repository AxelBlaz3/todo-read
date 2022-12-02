from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId
from bson import ObjectId

class Todo(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    content: str = Field(min_length=1)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
