# app/utils/login/login.py
from PyQt5.QtWidgets import QMainWindow
from app.models.database import SessionLocal
from app.models.user import User
from app.utils.security import verify_password
from app.ui.loginWindow.loginWindow import Ui_loginWindow
# Import the custom RecuperaPasswordWindow handler
from app.utils.login.recuperoHandler import RecuperaPasswordWindow #


class LoginWindow(QMainWindow):
    def __init__(self, on_success):
        super().__init__()
        self.ui = Ui_loginWindow()
        self.ui.setupUi(self)
        self.db = SessionLocal()
        self.on_success = on_success

        # Connessione dei pulsanti
        self.ui.login_button.clicked.connect(self.handle_login)
        self.ui.reset_password_button.clicked.connect(self.show_recupera_password)

        # variabile per mantenere riferimento alla finestra di recupero
        self.recupera_window = None

    def handle_login(self):
        email = self.ui.email_input.text()
        password = self.ui.password_input.text()

        user = self.db.query(User).filter(User.email == email).first()
        if user and verify_password(password, user.hashed_password):
            self.on_success(user)
            self.close()
        else:
            self.ui.error_label.setText("Email o password non validi")

    def show_recupera_password(self):
        """Mostra la finestra di recupero password"""
        self.hide()  # Nasconde la finestra di login
        # Instantiate RecuperaPasswordWindow from recuperoHandler.py, passing the callback
        self.recupera_window = RecuperaPasswordWindow(self.show_login) #
        self.recupera_window.show()

    def show_login(self):
        """Mostra di nuovo la finestra di login"""
        if self.recupera_window:
            self.recupera_window.close()
        self.show()