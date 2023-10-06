from PySide6.QtWidgets import QWidget, QSplitter, QFormLayout, QSpinBox
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Slot, Qt, QObject, Signal, QTime
from ui_settingswidget import Ui_SettingsWidget
import json
import utils
import sys


with open('./config/parameters.json', 'r') as f:
    param = utils.json_object_to_object(json.load(f))

class LogManager(QObject):
    appendLog = Signal(str)
    flushed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def write(self, text):
        if text != '\n':
            self.appendLog.emit(
                ' '.join([QTime.currentTime().toString('hh:mm:ss'), str(text)]) + '\n')
    
    def flush(self):
        pass

class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)
        self.ui.splitter.setStretchFactor(0, 9)
        self.ui.splitter.setStretchFactor(1, 0)
        splitter: QSplitter = self.ui.paramWidget.findChild(QSplitter, 'paramSplitter')
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 5)
        self.log = LogManager(self)
        self.log.appendLog.connect(self.appendLog)
        paramPanel = self.ui.paramPanel
        paramPanel.setLayout(QFormLayout())
        self.ui.pacingModeBox.currentTextChanged.connect(self.loadPacingModeParameters)
        self.ui.pacingModeBox.addItems(param.modes.__dict__.keys())
        for i in range(self.ui.pacingModeBox.count()):
            self.ui.pacingModeBox.setItemData(i, param.modes.__dict__.get(self.ui.pacingModeBox.itemText(i)).description, Qt.ItemDataRole.ToolTipRole)
        sys.stdout = self.log

    

    @Slot(str)
    def loadPacingModeParameters(self, pacingMode: str) -> None:
        print(f'loading {pacingMode} parameters')
        paramPanel = self.ui.paramPanel
        layout = paramPanel.layout()
        while layout.count():
            layout.removeRow(0)
        parameters = param.modes.__dict__.get(pacingMode).parameters
        for parameter in parameters:
            name, value, units = parameter.name, parameter.value, parameter.units
            box = QSpinBox()
            box.setValue(value)
            layout.addRow(f'{name} ({units})', box)
        paramPanel.setLayout(layout)

    @Slot(str)
    def appendLog(self, text:str):
        c = self.ui.textEdit.textCursor()
        c.movePosition(QTextCursor.End)
        c.insertText(text)
        self.ui.textEdit.setTextCursor(c)
        self.ui.textEdit.ensureCursorVisible()

    def destroy(self, destroyWindow: bool = ..., destroySubWindows: bool = ...) -> None:
        sys.stdout = sys.__stdout__
        return super().destroy(destroyWindow, destroySubWindows)