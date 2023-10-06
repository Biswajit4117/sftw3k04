from PySide6.QtWidgets import QWidget
from ui_modeselection import Ui_ModeSelection

class ModeSelection(QWidget):
    def __init__(self, parent=None, username=''):
        super().__init__(parent)
        self.ui = Ui_ModeSelection()
        self.ui.setupUi(self)
        self.ui.label.setText(f'Welcome, {username}')