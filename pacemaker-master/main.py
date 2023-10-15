from PySide6.QtWidgets import QApplication, QWidget
from modeselection import ModeSelection
from login import Login
#from qt_material import apply_stylesheet

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    from database import initDb
    initDb()
    window = ModeSelection(None)
    login = Login(None)
    login.exec()
    window.ui.label.setText(f'Welcome, {login.username}')
    # apply_stylesheet(app, 'dark_amber.xml')
    window.show()
    def relogin():
        window.close()
        login.exec()
        window.ui.label.setText(f'Welcome, {login.username}')
        window.show()
    window.ui.logoutButton.clicked.connect(relogin)
    sys.exit(app.exec())