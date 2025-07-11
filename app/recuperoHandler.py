from PyQt5.QtWidgets import QMainWindow
from app.ui.recuperaPasswordWindow.recuperaPasswordWindow import Ui_recuperaPasswordWindow

class RecuperaPasswordWindow(QMainWindow):
    def __init__(self, on_back):
        super().__init__()
        self.ui = Ui_recuperaPasswordWindow()
        self.ui.setupUi(self)
        self.on_back = on_back  # Callback per tornare al login

        # Connessione dei pulsanti
        self.ui.back_button.clicked.connect(self.handle_back)
        self.ui.recupera_button.clicked.connect(self.handle_recupera)

    def handle_recupera(self):
        email = self.ui.email_input.text()
        # Qui dovresti implementare la logica di recupero password
        # Per ora mostriamo solo un messaggio
        self.ui.error_label.setText("Email di recupero inviata a " + email)

    def handle_back(self):
        """Torna alla finestra di login"""
        self.on_back()
        self.close()