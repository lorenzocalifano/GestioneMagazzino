from enum import Enum
from sqlalchemy import Column, String, Enum as SQLAlchemyEnum, Integer
from app.models.database import Base
from app.utils.security import verify_password, hash_password

class RuoloEnum(str, Enum):
    LAVORATORE = "Lavoratore"
    SEGRETERIA = "Segreteria"
    RESPONSABILE = "Responsabile"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    cognome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    ruolo = Column(SQLAlchemyEnum(RuoloEnum), default=RuoloEnum.LAVORATORE, nullable=False)

    @classmethod
    def get_by_email(cls, db, email: str):
        return db.query(cls).filter(cls.email == email).first()

    def verify_password(self, plain_password: str) -> bool:
        return verify_password(plain_password, self.hashed_password)