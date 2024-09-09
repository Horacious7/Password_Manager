import sys
sys.path.append(r"C:\Users\maier\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages")
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)

        self.centralwidget = QWidget(MainWindow)
        self.verticalLayout = QVBoxLayout(self.centralwidget)

    
        self.username_input = QLineEdit(self.centralwidget)
        self.password_input = QLineEdit(self.centralwidget)
        self.password_input.setEchoMode(QLineEdit.Password)  

        self.add_button = QPushButton("Add Password", self.centralwidget)
        self.view_button = QPushButton("View Passwords", self.centralwidget)
        self.delete_button = QPushButton("Delete Password", self.centralwidget)

        self.password_display = QTextEdit(self.centralwidget)
        self.password_display.setReadOnly(True)  

        
        self.verticalLayout.addWidget(self.username_input)
        self.verticalLayout.addWidget(self.password_input)
        self.verticalLayout.addWidget(self.add_button)
        self.verticalLayout.addWidget(self.view_button)
        self.verticalLayout.addWidget(self.delete_button)
        self.verticalLayout.addWidget(self.password_display)

        MainWindow.setCentralWidget(self.centralwidget)
