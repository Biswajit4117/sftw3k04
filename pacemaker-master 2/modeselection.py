from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from ui_modeselection import Ui_ModeSelection
from login import Login
import utils
import serial as s
import serial.tools.list_ports


class ModeSelection(QWidget):
    def __init__(self, parent=None, username=''):
        super().__init__(parent)
        self.ui = Ui_ModeSelection()  # 创建对象，加载ui布局
        self.ui.setupUi(self)  # 将用户界面布局应用到当前窗口对象
        self.ui.label.setText(f'Welcome, {username}')
        # self.ui.logoutButton.clicked.connect(self.logout)

    def logout(self):
        print('logout')
        self.hide()
        login = Login(None)
        login.success.connect(self.onLogin)
        login.show()

    def onLogin(self, username):
        self.ui.label.setText(f'Welcome, {username}')
        self.show()
