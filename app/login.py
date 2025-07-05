from PyQt5.QtWidgets import QMainWindow
from app.models.database import SessionLocal
from app.models.user import User
from app.utils.security import verify_password
from app.ui.loginWindow.loginWindow import Ui_loginWindow

class LoginWindow(QMainWindow):
    def __init__(self, on_success):
        super().__init__()
        self.ui = Ui_loginWindow()
        self.ui.setupUi(self)
        self.db = SessionLocal()
        self.on_success = on_success

        self.ui.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        email = self.ui.email_input.text()
        password = self.ui.password_input.text()

        user = self.db.query(User).filter(User.email == email).first()
        if user and verify_password(password, user.hashed_password):
            self.on_success(user)
            self.close()
        else:
            self.ui.error_label.setText("Email o password non validi")