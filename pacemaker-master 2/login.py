from PySide6.QtWidgets import QDialog, QMessageBox  # qdia对话框，显示消息框
from PySide6.QtCore import Slot, Signal  # 用于处理qt信号与槽的机制，允许事件发生时执行特定的函数
from PySide6.QtSql import QSqlDatabase, QSqlError, QSqlQuery
from ui_login import Ui_Login
from registerdialog import RegisterDialog


class Login(QDialog):
    success = Signal(str)  # 登录成功时发出信号

    def __init__(self, parent=None):  # 初始化登录界面，使用uil来设置ui元素
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.username = ''  # 用于存储登录成功后的用户名

    def accept(self) -> None:  # 点击对话框ok，调用
        if self.__login():
            return super().accept()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def reject(self) -> None:  # 取消键调用
        import sys
        sys.exit(0)  # 退出程序

    def __login(self) -> None:  # 验证用户的登录凭据
        db = QSqlDatabase.database("pmdatabase")  # 获取数据库连接对象db，然后执行一个sql查询，查询是否存在与输入的用户名和密码匹配的记录
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

    def register(self):  # 创建一个registerdialog对象，并执行该对话框，用户可以在注册对话框中输入新的用户名和密码
        r = RegisterDialog(self)
        r.exec()
        return
