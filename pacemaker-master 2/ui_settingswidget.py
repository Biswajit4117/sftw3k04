# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingswidget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QPushButton, QScrollArea, QSizePolicy, QSplitter,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(779, 542)
        self.gridLayout_2 = QGridLayout(SettingsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter = QSplitter(SettingsWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.paramWidget = QWidget(self.splitter)
        self.paramWidget.setObjectName(u"paramWidget")
        self.gridLayout_3 = QGridLayout(self.paramWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.paramWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.historyBox = QGroupBox(self.widget)
        self.historyBox.setObjectName(u"historyBox")

        self.verticalLayout_2.addWidget(self.historyBox)

        self.deviceBox = QGroupBox(self.widget)
        self.deviceBox.setObjectName(u"deviceBox")

        self.verticalLayout_2.addWidget(self.deviceBox)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.paramSplitter = QSplitter(self.paramWidget)
        self.paramSplitter.setObjectName(u"paramSplitter")
        self.paramSplitter.setOrientation(Qt.Horizontal)
        self.paramBox = QGroupBox(self.paramSplitter)
        self.paramBox.setObjectName(u"paramBox")
        self.verticalLayout = QVBoxLayout(self.paramBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.comboBox = QComboBox(self.paramBox)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(400, 0))
        self.comboBox.setMaximumSize(QSize(400, 16777215))
        self.comboBox.setBaseSize(QSize(300, 0))

        self.verticalLayout.addWidget(self.comboBox)

        self.pushButton_open_serial = QPushButton(self.paramBox)
        self.pushButton_open_serial.setObjectName(u"pushButton_open_serial")
        sizePolicy.setHeightForWidth(self.pushButton_open_serial.sizePolicy().hasHeightForWidth())
        self.pushButton_open_serial.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton_open_serial)

        self.pushButton_refresh = QPushButton(self.paramBox)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")
        self.pushButton_refresh.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout.addWidget(self.pushButton_refresh)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.paramBox)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label)

        self.pacingModeBox = QComboBox(self.paramBox)
        self.pacingModeBox.setObjectName(u"pacingModeBox")

        self.horizontalLayout.addWidget(self.pacingModeBox)

        self.pushButton = QPushButton(self.paramBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.paramBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.paramPanel = QWidget()
        self.paramPanel.setObjectName(u"paramPanel")
        self.paramPanel.setGeometry(QRect(0, 0, 624, 69))
        self.scrollArea.setWidget(self.paramPanel)

        self.verticalLayout.addWidget(self.scrollArea)

        self.paramSplitter.addWidget(self.paramBox)

        self.gridLayout_3.addWidget(self.paramSplitter, 0, 1, 1, 1)

        self.splitter.addWidget(self.paramWidget)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)

        self.splitter.addWidget(self.groupBox)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Form", None))
        self.historyBox.setTitle(QCoreApplication.translate("SettingsWidget", u"History", None))
        self.deviceBox.setTitle(QCoreApplication.translate("SettingsWidget", u"Devices", None))
        self.paramBox.setTitle(QCoreApplication.translate("SettingsWidget", u"Set New Parameters", None))
        self.pushButton_open_serial.setText(QCoreApplication.translate("SettingsWidget", u"Open Serial", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("SettingsWidget", u"Refresh", None))
        self.label.setText(QCoreApplication.translate("SettingsWidget", u"Pacing Mode", None))
        self.pushButton.setText(QCoreApplication.translate("SettingsWidget", u"Send Serial", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsWidget", u"Console", None))
    # retranslateUi

