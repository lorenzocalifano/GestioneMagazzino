from app.models.database import Base, engine, SessionLocal
from app.models.user import User
from app.utils.security import hash_password

def init_db():
    # Elimina e ricrea tutte le tabelle
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Aggiungi un utente di test
    db = SessionLocal()
    try:
        user = User(
            name="Lorenzo",
            email="lorenzo@example.com",
            hashed_password=hash_password("password123")
        )
        db.add(user)
        db.commit()
        print("Database inizializzato con successo!")
    except Exception as e:
        db.rollback()
        print(f"Errore durante l'inizializzazione: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    init_db()