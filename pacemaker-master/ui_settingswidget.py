# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingswidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QScrollArea, QSizePolicy, QSplitter, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(541, 386)
        self.gridLayout_2 = QGridLayout(SettingsWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter = QSplitter(SettingsWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.paramWidget = QWidget(self.splitter)
        self.paramWidget.setObjectName(u"paramWidget")
        self.gridLayout_3 = QGridLayout(self.paramWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.paramSplitter = QSplitter(self.paramWidget)
        self.paramSplitter.setObjectName(u"paramSplitter")
        self.paramSplitter.setOrientation(Qt.Horizontal)
        self.historyBox = QGroupBox(self.paramSplitter)
        self.historyBox.setObjectName(u"historyBox")
        self.paramSplitter.addWidget(self.historyBox)
        self.paramBox = QGroupBox(self.paramSplitter)
        self.paramBox.setObjectName(u"paramBox")
        self.verticalLayout = QVBoxLayout(self.paramBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.paramBox)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.pacingModeBox = QComboBox(self.paramBox)
        self.pacingModeBox.setObjectName(u"pacingModeBox")

        self.horizontalLayout.addWidget(self.pacingModeBox)

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
        self.paramPanel.setGeometry(QRect(0, 0, 230, 99))
        self.scrollArea.setWidget(self.paramPanel)

        self.verticalLayout.addWidget(self.scrollArea)

        self.paramSplitter.addWidget(self.paramBox)

        self.gridLayout_3.addWidget(self.paramSplitter, 0, 0, 1, 1)

        self.splitter.addWidget(self.paramWidget)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.splitter.addWidget(self.groupBox)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Form", None))
        self.historyBox.setTitle(QCoreApplication.translate("SettingsWidget", u"History", None))
        self.paramBox.setTitle(QCoreApplication.translate("SettingsWidget", u"Set New Parameters", None))
        self.label.setText(QCoreApplication.translate("SettingsWidget", u"Pacing Mode", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsWidget", u"Console", None))
    # retranslateUi

