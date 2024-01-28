from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    name: str
    email: str
    mobile: str