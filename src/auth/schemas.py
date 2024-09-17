# This is a sample schemas.py file
from pydantic import BaseModel

class RequestLogin(BaseModel):
    username: str
    password: str
    
class ResponseLogin(BaseModel):
    access_token: str
    refresh_token: str
