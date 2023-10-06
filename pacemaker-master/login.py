from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlError, QSqlQuery
from ui_login import Ui_Login
from registerdialog import RegisterDialog

class Login(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.username = ''
    

    def accept(self) -> None:
        if self.__login():
            return super().accept()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")
    
    def reject(self) -> None:
        import sys
        sys.exit(0)
    
    def __login(self) -> None:
        db = QSqlDatabase.database("pmdatabase")
        get_user_sql = "select * from users where username = :name and password = :password"
        q = QSqlQuery(db)
        q.prepare(get_user_sql)
        print(self.ui.userName.text(), self.ui.password.text())
        q.bindValue(':name', self.ui.userName.text())
        q.bindValue(':password', self.ui.password.text())
        q.exec()
        if q.next():
            self.username = q.value(0)
            print(q.value(0), q.value(1))
            return True
        return False
    
    def register(self):
        r = RegisterDialog(self)
        r.exec()
        return
