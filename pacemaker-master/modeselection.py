from PySide6.QtWidgets import QWidget
from ui_modeselection import Ui_ModeSelection
from login import Login

class ModeSelection(QWidget):
    def __init__(self, parent=None, username=''):
        super().__init__(parent)
        self.ui = Ui_ModeSelection()
        self.ui.setupUi(self)
        self.ui.label.setText(f'Welcome, {username}')
        # self.ui.logoutButton.clicked.connect(self.logout)
    
    def logout(self):
        self.hide()
        login = Login(None)
        login.success.connect(self.onLogin)
        login.show()
    
    def onLogin(self, username):
        self.ui.label.setText(f'Welcome, {username}')
        self.show()