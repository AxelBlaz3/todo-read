from bson import ObjectId

class PyObjectId(ObjectId):
    """Class for handling MongoDB ObjectId."""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    # Method for validating an ObjectId.
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    # Method for updating the ObjectId to string.
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")