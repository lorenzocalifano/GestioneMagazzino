import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from app.models.database import SessionLocal, engine, Base
from app.models.user import User
from app.utils.security import verify_password, hash_password
from app.schemas.user_schema import UserCreate
from app.login import LoginWindow
from app.ui.main_window import Ui_MainWindow

#Crea tabelle nel database (da rimuovere in prod)
Base.metadata.create_all(bind=engine)
Base.metadata.drop_all(bind=engine)

db = SessionLocal()
new_user = User(
    name="Lorenzo",
    email="lorenzo@example.com",
    hashed_password=hash_password("password123")
)
db.add(new_user)
db.commit()

class MainApp(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = user  # Utente loggato
        self.db = SessionLocal()
        self.setWindowTitle(f"Benvenuto {self.user.name}")

    def save_user(self):
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

def start_app():
    import sys
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
