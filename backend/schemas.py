from pydantic import BaseModel

class UserInput(BaseModel):
    bio: str
    event: str
    interests: str