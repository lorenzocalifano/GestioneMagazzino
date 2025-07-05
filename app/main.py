import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from app.models.database import SessionLocal, engine, Base
from app.models.user import User
from app.utils.security import verify_password, hash_password
from app.schemas.user_schema import UserCreate
from app.login import LoginWindow
from app.ui.main_window import Ui_MainWindow as MainApp


def initialize_database():
    """Crea tutte le tabelle e aggiunge un utente di test"""
    # Crea le tabelle
    Base.metadata.create_all(bind=engine)

    # Aggiungi utente di test solo se non esiste
    db = SessionLocal()
    try:
        if not db.query(User).filter(User.email == "lorenzo@example.com").first():
            test_user = User(
                name="Lorenzo",
                email="lorenzo@example.com",
                hashed_password=hash_password("password123")
            )
            db.add(test_user)
            db.commit()
            print("Database inizializzato con utente di test")
    except Exception as e:
        print(f"Errore inizializzazione database: {e}")
        db.rollback()
    finally:
        db.close()

def start_app():
    # Prima inizializza il database
    initialize_database()

    # Poi avvia l'applicazione
    app = QApplication(sys.argv)

    def on_login_success(user):
        window = MainApp(user)
        window.show()
        app.exec_()

    login = LoginWindow(on_login_success)
    login.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start_app()

