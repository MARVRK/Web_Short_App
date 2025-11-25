from pydantic import BaseModel

class CreateUser(BaseModel):
    user_name : str