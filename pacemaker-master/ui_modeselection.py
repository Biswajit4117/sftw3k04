# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modeselection.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

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

        self.horizontalLayout_2.addWidget(self.label)


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
    # retranslateUi

