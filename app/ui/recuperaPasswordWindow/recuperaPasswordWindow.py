# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_recuperaPasswordWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setStyleSheet("background-color: #1E90FF;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Titolo
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 70, 750, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white; qproperty-alignment: AlignCenter;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # Email input
        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(240, 220, 271, 30))
        self.email_input.setStyleSheet("""
            background-color: white; 
            color: #1E90FF;
            padding: 5px;
            border-radius: 3px;
        """)
        self.email_input.setPlaceholderText("Email")

        # Bottone Recupera Password
        self.recupera_button = QtWidgets.QPushButton(self.centralwidget)
        self.recupera_button.setGeometry(QtCore.QRect(240, 270, 271, 40))
        self.recupera_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #1E90FF;
                font-weight: bold;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #F0F0F0;
            }
        """)

        # Label errore
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(240, 320, 271, 30))
        self.error_label.setStyleSheet("""
            color: white;
            font-weight: bold;
            qproperty-alignment: AlignCenter;
        """)
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)

        # Bottone Ritorna al Login
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(240, 360, 271, 40))
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #1E90FF;
                font-weight: bold;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #F0F0F0;
            }
        """)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 42))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Recupera Password - EVENTICA"))
        self.label.setText(_translate("MainWindow", "EVENTICA"))
        self.recupera_button.setText(_translate("MainWindow", "Recupera Password"))
        self.back_button.setText(_translate("MainWindow", "Ritorna al Login"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # Load Montserrat font if available
    font_db = QtGui.QFontDatabase()
    if "Montserrat" not in font_db.families():
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        app.setFont(font)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_recuperaPasswordWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())