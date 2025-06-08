import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from app.ui.main_window import Ui_MainWindow # UI generata
from app.models.database import SessionLocal, engine
from app.models.user import User

#Crea tabelle nel database (da rimuovere in prod)
User.metadata.create_all(bind=engine)

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Esempio di connessione al database
        self.db = SessionLocal()

        self.ui.pushButton.clicked.connect(self.save_user)

    def save_user(self):
        #Esempio utilizzo Pydantic + SQLAlchemy
        from app.schemas.user_schema import UserCreate
        user_data = UserCreate(
            name=self.ui.name_input_text(),
            email=self.ui.email_input.text()
        )

        #Salva nel db
        db_user = User(**user_data.dict())
        self.db.add(db_user)
        self.db.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
