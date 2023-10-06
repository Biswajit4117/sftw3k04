from PySide6.QtWidgets import QApplication, QWidget
from modeselection import ModeSelection
from login import Login
#from qt_material import apply_stylesheet

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    from database import initDb
    initDb()
    login = Login(None)
    login.exec()
    # apply_stylesheet(app, 'dark_amber.xml')
    window = ModeSelection(None, login.username)
    window.show()
    sys.exit(app.exec())