# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'visualizationwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QScrollArea, QSizePolicy, QSplitter, QWidget)

class Ui_visualizationWidget(object):
    def setupUi(self, visualizationWidget):
        if not visualizationWidget.objectName():
            visualizationWidget.setObjectName(u"visualizationWidget")
        visualizationWidget.resize(400, 300)
        self.gridLayout = QGridLayout(visualizationWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(visualizationWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.allParamsGroup = QGroupBox(self.splitter)
        self.allParamsGroup.setObjectName(u"allParamsGroup")
        self.gridLayout_3 = QGridLayout(self.allParamsGroup)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.allParamsGroup)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.allParams = QWidget()
        self.allParams.setObjectName(u"allParams")
        self.allParams.setGeometry(QRect(0, 0, 362, 93))
        self.scrollArea.setWidget(self.allParams)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.splitter.addWidget(self.allParamsGroup)
        self.electrogramGroup = QGroupBox(self.splitter)
        self.electrogramGroup.setObjectName(u"electrogramGroup")
        self.gridLayout_2 = QGridLayout(self.electrogramGroup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter.addWidget(self.electrogramGroup)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.retranslateUi(visualizationWidget)

        QMetaObject.connectSlotsByName(visualizationWidget)
    # setupUi

    def retranslateUi(self, visualizationWidget):
        visualizationWidget.setWindowTitle(QCoreApplication.translate("visualizationWidget", u"Form", None))
        self.allParamsGroup.setTitle(QCoreApplication.translate("visualizationWidget", u"Pacemaker Parameters", None))
        self.electrogramGroup.setTitle(QCoreApplication.translate("visualizationWidget", u"Electrogram", None))
    # retranslateUi

