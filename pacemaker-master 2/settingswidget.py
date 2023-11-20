import time

from PySide6.QtWidgets import QWidget, QSplitter, QFormLayout, QSpinBox, QHBoxLayout, QLabel
from PySide6.QtGui import QTextCursor
from PySide6.QtCore import Slot, Qt, QObject, Signal, QTime, QDateTime
from ui_settingswidget import Ui_SettingsWidget
import json
import utils
import sys
import database
import serial as s

with open('./config/parameters.json', 'r') as f:  # 打开pj
    param = utils.json_object_to_object(json.load(f))  # 使用jlf将文件中的json数据加载到名为param的变量中


class LogManager(QObject):  # 定义一个子类，用来管理日志的显示和追加，下面两个信号
    appendLog = Signal(str)  # 用于追加日志文本
    flushed = Signal()  # 在清空日志时触发

    def __init__(self, parent=None):
        super().__init__(parent)  # 初始化父类

    def write(self, text):  # 将文本追加到日志中，它在文本不为空时触发appenlog，同时在文本前面添加时间戳
        if text != '\n':
            self.appendLog.emit(
                ' '.join([QDateTime.currentDateTime().toString('yyyy:MM:dd hh:mm:ss'), str(text)]) + '\n')

    def flush(self):
        pass


class SettingsWidget(QWidget):  # 子类，创建设置窗口
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsWidget()  # 加载用户的页面布局，通过下面的应用到当前窗口
        self.ui.setupUi(self)
        self.ui.splitter.setStretchFactor(0, 9)  # 设置窗口大小
        self.ui.splitter.setStretchFactor(1, 0)
        splitter: QSplitter = self.ui.paramWidget.findChild(QSplitter, 'paramSplitter')
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 5)
        self.log = LogManager(self)  # 创建了logmanager对象selflog,将信号appendlog信号连接到appendlog方法，实现将日志信息显示在窗口
        self.log.appendLog.connect(self.appendLog_Slot)
        paramPanel = self.ui.paramPanel
        paramPanel.setLayout(QFormLayout())  # 初始化了参数选择下拉框，selfpb，连接，实现选择不同的心脏起搏模式，加载相关参数
        self.ui.pacingModeBox.currentTextChanged.connect(self.loadPacingModeParameters)
        self.ui.pacingModeBox.addItems(param.modes.__dict__.keys())
        self.ui.deviceBox.setLayout(QHBoxLayout())  # 初始化设置列表sdb,
        for device in database.allDevices():  # 通过循环遍历数据库中的设备列表，并添加表情qlabel来显示设备
            self.ui.deviceBox.layout().addWidget(QLabel(device))
        for i in range(self.ui.pacingModeBox.count()):
            self.ui.pacingModeBox.setItemData(i,
                                              param.modes.__dict__.get(self.ui.pacingModeBox.itemText(i)).description,
                                              Qt.ItemDataRole.ToolTipRole)
        sys.stdout = self.log  # 最后将输出s重新定义到s,捕获应用程序的标准输出并将其显示在日志窗口

        # 槽函数
        self.ui.pushButton_open_serial.clicked.connect(self.open_serial())
        self.ui.pushButton_refresh.clicked.connect(self.refresh_port())
        self.__serial = None



    @Slot(str)
    def loadPacingModeParameters(self, pacingMode: str) -> None:  # 槽函数，在用户选择不同心脏起搏模式时加载相关参数，并在界面显示
        def sendParam(name):  # 嵌套函数，返回一个内部函数，用于在用户更改参数值时打印参数名称和新值
            def inner(value):
                print(f'{name} set to {value}')

            return inner

        print(f'loading {pacingMode} parameters')  # 打印一条日志，指示正在加载哪个心脏起搏器的参数
        paramPanel = self.ui.paramPanel
        layout = paramPanel.layout()  # 获取界面参数显示区域的布局layout
        while layout.count():  # 将现有的参数行从布局中删除，以便清空之前选择的参数
            layout.removeRow(0)
        parameters = param.modes.__dict__.get(pacingMode).parameters  # 从全局变量pmd获取心脏起搏模式的参数列表parameter
        for parameter in parameters:  # 遍历ps,并为每个参数创建一个带有初始值的qspinbox部件，用于接收用户输入或显示参数值
            name, value, units = parameter.name, parameter.value, parameter.units
            box = QSpinBox()  # 将每个部件值更改信号连接到sendpara函数，以便在值更改时触发参数名称和新值打印
            box.setValue(value)
            box.valueChanged.connect(sendParam(name))
            layout.addRow(f'{name} ({units})', box)  # 最后，将参数名称和qspinbox部件添加到界面中
        paramPanel.setLayout(layout)  # 更新参数显示区域的布局

    @Slot(str)
    def appendLog_Slot(self, text: str):  # 参数text是追加的文本
        c = self.ui.textEdit.textCursor()  # 获取文本编辑框的对象c
        c.movePosition(QTextCursor.End)  # 使用这个函数将光标移动到文本末尾的位置
        c.insertText(text)  # 将指定的文本插入到光标位置
        self.ui.textEdit.setTextCursor(c)  # 更新文本编辑框的光标位置，以便将滚动条滚动到最新的日志条目
        self.ui.textEdit.ensureCursorVisible()  # 确保光标可见

    def destroy(self, destroyWindow: bool = ..., destroySubWindows: bool = ...) -> None:
        sys.stdout = sys.__stdout__  # 将标准输出st恢复为系统的默认输出，以防止后续的输出被捕获
        return super().destroy(destroyWindow, destroySubWindows)  # 调用父类方法来执行窗口销毁

    def send_serial(self):
        content = self.ui.pacingModeBox.currentText()

        # writed = self.__serial.write(content)
        print('send serial: ' + content + ' success')

        time.sleep(0.5)
        # received_data = self.__serial.read(10)
        # print('recv: ' + received_data)


    # @Slot
    def refresh_port(self):
        self.ui.comboBox.clear()
        port_list = list(s.tools.list_ports.comports())
        devices = []
        for i in port_list:
            devices.append(i.device)
        print('port: ' + str(devices))
        self.ui.comboBox.addItems(devices)

    # @Slot
    def open_serial(self):
        print('openSerial: ')
        mode = self.ui.pacingModeBox.currentText()
        mode = 'COM3'
        self.__serial = s.Serial(port=mode, baudrate=9600, timeout=3)  # 根据你的实际情况修改串口号和波特率
        if self.__serial.isOpen():
            print('Open Success!!!!')
        else:
            print('Open Failed:' + mode)

        self.__serial.write(b'ADO')
