from app.models.user import User
from app.schemas.user_schema import UserCreate
from app.utils.security import hash_password

def create_user(db, user_data: UserCreate):
    db_user = User(
        nome=user_data.nome,
        cognome=user_data.cognome,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        ruolo=user_data.ruolo
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user