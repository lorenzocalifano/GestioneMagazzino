from pydantic import BaseModel, EmailStr
from app.models.user import RuoloEnum

class UserCreate(BaseModel):
    nome: str
    cognome: str
    email: EmailStr
    password: str
    ruolo: RuoloEnum = RuoloEnum.LAVORATORE

class UserResponse(BaseModel):
    id: int
    nome: str
    cognome: str
    email: str
    ruolo: RuoloEnum

    class Config:
        orm_mode = True