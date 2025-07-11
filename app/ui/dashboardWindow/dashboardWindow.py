# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dashboardWindow(object):
    def setupUi(self, MainWindow, user):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet("""
            * {
                font-family: 'Montserrat';
                font-weight: bold;
            }
            QMainWindow {
                background-color: #F0F2F5;
            }
            QWidget#centralwidget {
                background-color: #F0F2F5;
            }
            QLabel {
                color: #333333;
            }
            QPushButton {
                background-color: #1E90FF;
                color: white;
                border-radius: 5px;
                padding: 8px 15px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #187bcd;
            }
            QFrame#sidebar {
                background-color: #1E90FF;
                border-radius: 0;
            }
            QPushButton#menu_button {
                background-color: transparent;
                color: white;
                text-align: left;
                padding: 12px 20px;
                font-size: 16px;
                border-radius: 0;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }
            QPushButton#menu_button:hover {
                background-color: #187bcd;
            }
            QFrame#header {
                background-color: white;
                border-bottom: 1px solid #e0e0e0;
            }
            QFrame#widget_container {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
        """)

        self.user = user

        # Widget centrale
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Layout principale
        self.main_layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Sidebar
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setMinimumWidth(250)
        self.sidebar.setMaximumWidth(250)
        self.sidebar.setObjectName("sidebar")
        self.sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_layout.setSpacing(0)

        # Logo e titolo sidebar
        self.sidebar_header = QtWidgets.QFrame(self.sidebar)
        self.sidebar_header.setMinimumHeight(80)
        self.sidebar_header_layout = QtWidgets.QHBoxLayout(self.sidebar_header)

        self.logo_label = QtWidgets.QLabel(self.sidebar_header)
        self.logo_label.setMinimumSize(50, 50)
        self.logo_label.setMaximumSize(50, 50)
        self.logo_label.setStyleSheet("background-color: white; border-radius: 25px;")

        self.sidebar_title = QtWidgets.QLabel(self.sidebar_header)
        self.sidebar_title.setText("EVENTICA")
        self.sidebar_title.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")

        self.sidebar_header_layout.addWidget(self.logo_label)
        self.sidebar_header_layout.addWidget(self.sidebar_title)
        self.sidebar_header_layout.addStretch()

        self.sidebar_layout.addWidget(self.sidebar_header)

        # Menu laterale
        self.menu_frame = QtWidgets.QFrame(self.sidebar)
        self.menu_layout = QtWidgets.QVBoxLayout(self.menu_frame)
        self.menu_layout.setContentsMargins(0, 20, 0, 20)
        self.menu_layout.setSpacing(0)

        # Bottoni del menu
        self.dashboard_btn = QtWidgets.QPushButton(self.menu_frame)
        self.dashboard_btn.setObjectName("menu_button")
        self.dashboard_btn.setText("Dashboard")
        self.dashboard_btn.setIcon(QtGui.QIcon(":/icons/dashboard.png"))

        self.prodotti_btn = QtWidgets.QPushButton(self.menu_frame)
        self.prodotti_btn.setObjectName("menu_button")
        self.prodotti_btn.setText("Gestione Prodotti")
        self.prodotti_btn.setIcon(QtGui.QIcon(":/icons/products.png"))

        self.noleggi_btn = QtWidgets.QPushButton(self.menu_frame)
        self.noleggi_btn.setObjectName("menu_button")
        self.noleggi_btn.setText("Gestione Noleggi/Vendite")
        self.noleggi_btn.setIcon(QtGui.QIcon(":/icons/rentals.png"))

        self.utenti_btn = QtWidgets.QPushButton(self.menu_frame)
        self.utenti_btn.setObjectName("menu_button")
        self.utenti_btn.setText("Gestione Utenti")
        self.utenti_btn.setIcon(QtGui.QIcon(":/icons/users.png"))

        self.storico_btn = QtWidgets.QPushButton(self.menu_frame)
        self.storico_btn.setObjectName("menu_button")
        self.storico_btn.setText("Storico Operazioni")
        self.storico_btn.setIcon(QtGui.QIcon(":/icons/history.png"))

        self.menu_layout.addWidget(self.dashboard_btn)
        self.menu_layout.addWidget(self.prodotti_btn)
        self.menu_layout.addWidget(self.noleggi_btn)

        # Mostra Gestione Utenti solo per Responsabili
        if user.ruolo == "Responsabile":
            self.menu_layout.addWidget(self.utenti_btn)

        self.menu_layout.addWidget(self.storico_btn)
        self.menu_layout.addStretch()

        # Logout button
        self.logout_btn = QtWidgets.QPushButton(self.menu_frame)
        self.logout_btn.setObjectName("menu_button")
        self.logout_btn.setText("Logout")
        self.logout_btn.setIcon(QtGui.QIcon(":/icons/logout.png"))
        self.menu_layout.addWidget(self.logout_btn)

        self.sidebar_layout.addWidget(self.menu_frame)
        self.main_layout.addWidget(self.sidebar)

        # Area principale
        self.main_area = QtWidgets.QWidget(self.centralwidget)
        self.main_layout.addWidget(self.main_area)

        # Layout area principale
        self.main_area_layout = QtWidgets.QVBoxLayout(self.main_area)
        self.main_area_layout.setContentsMargins(20, 20, 20, 20)
        self.main_area_layout.setSpacing(20)

        # Header
        self.header = QtWidgets.QFrame(self.main_area)
        self.header.setObjectName("header")
        self.header.setMinimumHeight(70)
        self.header_layout = QtWidgets.QHBoxLayout(self.header)

        self.title_label = QtWidgets.QLabel(self.header)
        self.title_label.setText("Dashboard")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        self.user_info = QtWidgets.QLabel(self.header)
        self.user_info.setText(f"{user.nome} {user.cognome} | {user.ruolo}")
        self.user_info.setStyleSheet("font-size: 16px;")

        self.header_layout.addWidget(self.title_label)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.user_info)

        self.main_area_layout.addWidget(self.header)

        # Widget riepilogativi
        self.widgets_container = QtWidgets.QFrame(self.main_area)
        self.widgets_container.setObjectName("widget_container")
        self.widgets_layout = QtWidgets.QHBoxLayout(self.widgets_container)

        # Widget Prodotti in esaurimento
        self.widget_prodotti = QtWidgets.QFrame(self.widgets_container)
        self.widget_prodotti.setStyleSheet("""
            background-color: #FFF8E1;
            border-radius: 10px;
            padding: 15px;
        """)
        self.widget_prodotti_layout = QtWidgets.QVBoxLayout(self.widget_prodotti)

        self.prodotti_title = QtWidgets.QLabel(self.widget_prodotti)
        self.prodotti_title.setText("Prodotti in esaurimento")
        self.prodotti_title.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.prodotti_list = QtWidgets.QListWidget(self.widget_prodotti)
        self.prodotti_list.addItems(
            ["Prodotto A - Quantità: 2", "Prodotto B - Quantità: 3", "Prodotto C - Quantità: 1"])

        self.widget_prodotti_layout.addWidget(self.prodotti_title)
        self.widget_prodotti_layout.addWidget(self.prodotti_list)

        # Widget Noleggi attivi
        self.widget_noleggi = QtWidgets.QFrame(self.widgets_container)
        self.widget_noleggi.setStyleSheet("""
            background-color: #E8F5E9;
            border-radius: 10px;
            padding: 15px;
        """)
        self.widget_noleggi_layout = QtWidgets.QVBoxLayout(self.widget_noleggi)

        self.noleggi_title = QtWidgets.QLabel(self.widget_noleggi)
        self.noleggi_title.setText("Noleggi attivi")
        self.noleggi_title.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.noleggi_list = QtWidgets.QListWidget(self.widget_noleggi)
        self.noleggi_list.addItems(["Noleggio #123 - Cliente: Mario Rossi", "Noleggio #124 - Cliente: Luca Bianchi"])

        self.widget_noleggi_layout.addWidget(self.noleggi_title)
        self.widget_noleggi_layout.addWidget(self.noleggi_list)

        # Widget Segnalazioni recenti
        self.widget_segnalazioni = QtWidgets.QFrame(self.widgets_container)
        self.widget_segnalazioni.setStyleSheet("""
            background-color: #FFEBEE;
            border-radius: 10px;
            padding: 15px;
        """)
        self.widget_segnalazioni_layout = QtWidgets.QVBoxLayout(self.widget_segnalazioni)

        self.segnalazioni_title = QtWidgets.QLabel(self.widget_segnalazioni)
        self.segnalazioni_title.setText("Segnalazioni recenti")
        self.segnalazioni_title.setStyleSheet("font-size: 18px; font-weight: bold;")

        self.segnalazioni_list = QtWidgets.QListWidget(self.widget_segnalazioni)
        self.segnalazioni_list.addItems(
            ["Segnalazione #45 - Prodotto danneggiato", "Segnalazione #46 - Consegna in ritardo"])

        self.widget_segnalazioni_layout.addWidget(self.segnalazioni_title)
        self.widget_segnalazioni_layout.addWidget(self.segnalazioni_list)

        self.widgets_layout.addWidget(self.widget_prodotti)
        self.widgets_layout.addWidget(self.widget_noleggi)
        self.widgets_layout.addWidget(self.widget_segnalazioni)

        self.main_area_layout.addWidget(self.widgets_container)

        # Area contenuto principale
        self.content_area = QtWidgets.QStackedWidget(self.main_area)
        self.main_area_layout.addWidget(self.content_area)

        # Pagina dashboard (vuota per ora)
        self.dashboard_page = QtWidgets.QWidget()
        self.content_area.addWidget(self.dashboard_page)

        # Pagina gestione prodotti (placeholder)
        self.prodotti_page = QtWidgets.QWidget()
        self.prodotti_page_layout = QtWidgets.QVBoxLayout(self.prodotti_page)
        self.prodotti_page_layout.addWidget(QtWidgets.QLabel("Gestione Prodotti - Pagina in costruzione"))
        self.content_area.addWidget(self.prodotti_page)

        # Pagina gestione noleggi (placeholder)
        self.noleggi_page = QtWidgets.QWidget()
        self.noleggi_page_layout = QtWidgets.QVBoxLayout(self.noleggi_page)
        self.noleggi_page_layout.addWidget(QtWidgets.QLabel("Gestione Noleggi/Vendite - Pagina in costruzione"))
        self.content_area.addWidget(self.noleggi_page)

        # Pagina gestione utenti (placeholder)
        self.utenti_page = QtWidgets.QWidget()
        self.utenti_page_layout = QtWidgets.QVBoxLayout(self.utenti_page)
        self.utenti_page_layout.addWidget(QtWidgets.QLabel("Gestione Utenti - Pagina in costruzione"))
        self.content_area.addWidget(self.utenti_page)

        # Pagina storico operazioni (placeholder)
        self.storico_page = QtWidgets.QWidget()
        self.storico_page_layout = QtWidgets.QVBoxLayout(self.storico_page)
        self.storico_page_layout.addWidget(QtWidgets.QLabel("Storico Operazioni - Pagina in costruzione"))
        self.content_area.addWidget(self.storico_page)

        # Imposta la pagina dashboard come predefinita
        self.content_area.setCurrentIndex(0)

        MainWindow.setCentralWidget(self.centralwidget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        MainWindow.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard - EVENTICA"))


if __name__ == "__main__":
    import sys
    from app.models.user import User

    # Creazione utente di esempio
    class MockUser:
        def __init__(self):
            self.nome = "Mario"
            self.cognome = "Rossi"
            self.ruolo = "Responsabile"


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_dashboardWindow()
    ui.setupUi(MainWindow, MockUser())
    MainWindow.show()
    sys.exit(app.exec_())