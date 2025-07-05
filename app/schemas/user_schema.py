from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True