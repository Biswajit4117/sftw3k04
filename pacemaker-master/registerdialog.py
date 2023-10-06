from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtSql import QSqlError
from database import insertUser

from ui_registerdialog import Ui_registerDialog

class RegisterDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_registerDialog()
        self.ui.setupUi(self)
    
    def accept(self) -> None:
        userName = self.ui.userName.text()
        password = self.ui.newPassword.text()
        passwordRepeat = self.ui.repeatPassword.text()
        if password != passwordRepeat:
            QMessageBox.warning(self, "Register Failed", "Passwords do not match")
            return
        if len(password) < 10:
            QMessageBox.warning(self, "Register Failed", "Password must be at least 10 characters")
            return
        if len(userName) < 5:
            QMessageBox.warning(self, "Register Failed", "Username must be at least 5 characters")
            return
        if insertUser(userName, password).type() != QSqlError.ErrorType.NoError:
            QMessageBox.warning(self, "Register Failed", f"Error type: {insertUser(userName, password).type()}")
            return
        QMessageBox.information(self, "Register Success", "Register Success")
        super().accept()