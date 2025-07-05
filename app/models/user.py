from sqlalchemy import Column, Integer, String
from .database import Base
from app.utils.security import hash_password, verify_password


def save_user(self):
    from app.schemas.user_schema import UserCreate
    user_data = UserCreate(
        name=self.ui.name_input.text(),
        email=self.ui.email_input.text(),
        password=self.ui.password_input.text()
    )

    db_user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
    )
    self.db.add(db_user)
    self.db.commit()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, index=True)

    @classmethod
    def get_by_email(cls, db, email: str):
        return db.query(cls).filter(cls.email == email).first()

    def verify_password(self, plain_password: str) -> bool:
        return verify_password(plain_password, self.hashed_password)