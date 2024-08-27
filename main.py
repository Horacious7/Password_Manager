import sys
sys.path.append(r"C:\Users\maier\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages")
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QVBoxLayout, QPushButton, QListWidget, QLabel
from ui_mainwindow import Ui_MainWindow
from password_manager import PasswordManager


class DeletePasswordDialog(QDialog):
    def __init__(self, password_manager):
        super(DeletePasswordDialog, self).__init__()
        self.password_manager = password_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Delete Password")
        layout = QVBoxLayout(self)
        self.list_widget = QListWidget(self)
        self.update_list()
        self.delete_button = QPushButton("Delete Selected Password", self)
        self.delete_button.clicked.connect(self.delete_password)
        layout.addWidget(QLabel("Select a password to delete:", self))
        layout.addWidget(self.list_widget)
        layout.addWidget(self.delete_button)
        self.setLayout(layout)

    def update_list(self):
        self.list_widget.clear()
        passwords = self.password_manager.view_passwords()
        for account, _ in passwords:
            self.list_widget.addItem(account)

    def delete_password(self):
        selected_items = self.list_widget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Error", "No account selected.")
            return

        account_to_delete = selected_items[0].text()
        try:
            self.password_manager.delete_password(account_to_delete)
            QMessageBox.information(self, "Success", f"Password for {account_to_delete} deleted successfully.")
            self.update_list()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to delete password: {e}")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.password_manager = PasswordManager()
        self.add_button.clicked.connect(self.add_password)
        self.view_button.clicked.connect(self.view_passwords)
        self.delete_button.clicked.connect(self.open_delete_dialog)

    def add_password(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username and password:
            try:
                self.password_manager.add_password(username, password)
                QMessageBox.information(self, "Success", "Password added successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to add password: {e}")
        else:
            QMessageBox.warning(self, "Input Error", "Please enter both username and password.")

    def view_passwords(self):
        try:
            self.password_display.clear()
            passwords = self.password_manager.view_passwords()
            for account, password in passwords:
                self.password_display.append(f"Account: {account}, Password: {password}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to view passwords: {e}")

    def open_delete_dialog(self):
        dialog = DeletePasswordDialog(self.password_manager)
        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
