# This is a sample model.py file
from pydantic import BaseModel

class CurrentUser(BaseModel):
    username: str
    password: str
    