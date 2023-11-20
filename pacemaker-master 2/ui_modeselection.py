# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modeselection.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from settingswidget import SettingsWidget
from visualizationwidget import VisualizationWidget

class Ui_ModeSelection(object):
    def setupUi(self, ModeSelection):
        if not ModeSelection.objectName():
            ModeSelection.setObjectName(u"ModeSelection")
        ModeSelection.resize(1276, 703)
        self.verticalLayout = QVBoxLayout(ModeSelection)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(ModeSelection)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.logoutButton = QPushButton(self.widget)
        self.logoutButton.setObjectName(u"logoutButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.logoutButton)


        self.verticalLayout.addWidget(self.widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.settingsWidget = SettingsWidget(ModeSelection)
        self.settingsWidget.setObjectName(u"settingsWidget")

        self.horizontalLayout.addWidget(self.settingsWidget)

        self.visualizationWidget = VisualizationWidget(ModeSelection)
        self.visualizationWidget.setObjectName(u"visualizationWidget")

        self.horizontalLayout.addWidget(self.visualizationWidget)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(ModeSelection)

        QMetaObject.connectSlotsByName(ModeSelection)
    # setupUi

    def retranslateUi(self, ModeSelection):
        ModeSelection.setWindowTitle(QCoreApplication.translate("ModeSelection", u"Mode", None))
        self.label.setText("")
        self.logoutButton.setText(QCoreApplication.translate("ModeSelection", u"Logout", None))
    # retranslateUi

