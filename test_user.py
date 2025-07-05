from app.models.database import SessionLocal
from app.models.user import User
from app.utils.security import hash_password

db = SessionLocal()

new_user = User(
    name="Lorenzo",
    email="lorenzo@example.com",
    hashed_password=hash_password("password123")
)

db.add(new_user)
db.commit()
print("Utente creato con successo!")