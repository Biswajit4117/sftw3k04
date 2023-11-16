from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Slot, Signal
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from ui_login import Ui_Login
from registerdialog import RegisterDialog

class Login(QDialog):
    MAX_LOGINS = 10
    active_logins = 0  # Class variable to track the number of active logins

    success = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.username = ''

    def accept(self) -> None:
        if Login.active_logins >= Login.MAX_LOGINS:
            QMessageBox.warning(self, "Login Failed", "Maximum number of users logged in")
            return

        if self.__login():
            Login.active_logins += 1  # Increment active logins count
            self.success.emit(self.username)  # Emitting the success signal with the username
            return super().accept()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def reject(self) -> None:
        import sys
        sys.exit(0)

    def __login(self) -> bool:
        db = QSqlDatabase.database("pmdatabase")
        get_user_sql = "select * from users where username = :name and password = :password"
        q = QSqlQuery(db)
        q.prepare(get_user_sql)
        q.bindValue(':name', self.ui.userName.text())
        q.bindValue(':password', self.ui.password.text())
        q.exec()
        if q.next():
            self.username = q.value(0)
            return True
        return False
    
    def register(self):
        r = RegisterDialog(self)
        r.exec()
        return

    def closeEvent(self, event):
        # Override to decrease the active logins count
        Login.active_logins -= 1
        super().closeEvent(event)
