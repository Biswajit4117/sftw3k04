from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtSql import QSqlError
from database import insertUser

from ui_registerdialog import Ui_registerDialog


class RegisterDialog(QDialog):  # 继承来自qdialog的对话框类，用于创建用户注册界面
    def __init__(self, parent=None) -> None:
        super().__init__(parent)  # 调用qdilog的构造函数，将parent参数传递给构造函数，确保正确的管理父窗口和对话框之间的关系
        self.ui = Ui_registerDialog()  # 创建一个用户界面对象，加载用户注册界面的ui布局
        self.ui.setupUi(self)  # 将用户界面应用到当前对话框

    def accept(self) -> None:
        userName = self.ui.userName.text()
        password = self.ui.newPassword.text()
        passwordRepeat = self.ui.repeatPassword.text()
        if password != passwordRepeat:
            QMessageBox.warning(self, "Register Failed", "Passwords do not match")
            return
        if len(password) > 10:
            QMessageBox.warning(self, "Register Failed", "Password must be less than 10 characters")
            return
        if len(userName) < 5:
            QMessageBox.warning(self, "Register Failed", "Username must be at least 5 characters")
            return
        if insertUser(userName, password).type() != QSqlError.ErrorType.NoError:
            QMessageBox.warning(self, "Register Failed", f"Error message: {insertUser(userName, password).text()}")
            return
        QMessageBox.information(self, "Register Success", "Register Success")
        super().accept()
